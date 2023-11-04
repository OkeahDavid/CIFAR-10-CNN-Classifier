# can be run to generate the .h5 file with the data
import tensorflow as tf
from data_preprocessing import load_and_preprocess_data
from model import create_cnn_model

(train_images, train_labels), (test_images, test_labels) = load_and_preprocess_data()
model = create_cnn_model()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

# Save the trained model
model.save("cnn_model.h5")
