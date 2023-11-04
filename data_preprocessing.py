import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical

def load_and_preprocess_data():
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
    
    # Normalize pixel values to be between 0 and 1
    train_images, test_images = train_images / 255.0, test_images / 255.0
    
    # One-hot encoding is optional. If you want to use it, uncomment the following lines:
    # train_labels = to_categorical(train_labels)
    # test_labels = to_categorical(test_labels)
    
    return (train_images, train_labels), (test_images, test_labels)
