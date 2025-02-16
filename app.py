from flask import Flask, request, render_template, redirect, url_for
import os
import cv2
import numpy as np
from model import create_model

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit

# Define the input shape (frames, height, width, channels)
input_shape = (None, 128, 128, 3)  # Example: Variable number of frames, 128x128 RGB images

# Create the model
model = create_model(input_shape)

# Load the weights (if they exist)
if os.path.exists('model_weights.h5'):
    model.load_weights('model_weights.h5')
    print("Model weights loaded successfully.")
else:
    print("Warning: 'model_weights.h5' not found. Using untrained model.")

def analyze_video(file_path):
    # Preprocess the video
    cap = cv2.VideoCapture(file_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (128, 128))
        frame = frame / 255.0  # Normalize
        frames.append(frame)
    cap.release()

    # Predict
    frames = np.array(frames)
    prediction = model.predict(np.expand_dims(frames, axis=0))
    return "Fake" if prediction > 0.5 else "Real"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return "No file uploaded", 400
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Analyze the video
    result = analyze_video(file_path)
    return redirect(url_for('result', result=result))

@app.route('/result')
def result():
    result = request.args.get('result', 'Unknown')
    return render_template('result.html', result=result)

@app.route('/remove_request', methods=['GET', 'POST'])
def remove_request():
    if request.method == 'POST':
        # Process removal request (e.g., send to cybersecurity agency)
        return "Removal request submitted successfully."
    return render_template('remove_request.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)