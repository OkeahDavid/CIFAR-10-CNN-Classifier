import tensorflow as tf
from data_preprocessing import load_and_preprocess_data

model = tf.keras.models.load_model("cnn_model.h5")

(_, _), (test_images, test_labels) = load_and_preprocess_data()
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
