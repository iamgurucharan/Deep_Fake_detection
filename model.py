import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, LSTM, Dense, Flatten, TimeDistributed

def create_model(input_shape):
    model = Sequential()

    # CNN Layers for spatial feature extraction
    model.add(TimeDistributed(Conv2D(32, (3, 3), activation='relu'), input_shape=input_shape))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    model.add(TimeDistributed(Conv2D(64, (3, 3), activation='relu')))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))
    model.add(TimeDistributed(Conv2D(128, (3, 3), activation='relu')))
    model.add(TimeDistributed(MaxPooling2D((2, 2))))

    # Flatten the output for RNN/LSTM
    model.add(TimeDistributed(Flatten()))

    # LSTM Layers for temporal feature extraction
    model.add(LSTM(64, return_sequences=True))
    model.add(LSTM(32))

    # Dense Layers for classification
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))  # Binary classification (real/fake)

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model