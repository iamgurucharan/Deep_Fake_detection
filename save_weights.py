from model import create_model

# Define the input shape (frames, height, width, channels)
input_shape = (None, 128, 128, 3)  # Example: Variable number of frames, 128x128 RGB images

# Create the model
model = create_model(input_shape)

# Save the model weights
model.save_weights('model_weights.h5')
print("Model weights saved to 'model_weights.h5'.")