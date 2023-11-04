import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
from utils import visualize_cifar10

# Define the predict_new_images function
def predict_new_images(model, new_images):
    predictions = model.predict(new_images)
    predicted_classes = np.argmax(predictions, axis=1)
    return predicted_classes

# Load the trained model
model_path = "cnn_model.h5"
model = tf.keras.models.load_model(model_path)

# Load the CIFAR-10 dataset
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# Use the predict_new_images function to predict on a subset of the training images
predicted_classes = predict_new_images(model, train_images[:25])

# Visualization function with predictions
def visualize_with_predictions(images, true_labels, predicted_labels):
    class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                   'dog', 'frog', 'horse', 'ship', 'truck']
    
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        true_label = class_names[true_labels[i][0]]
        pred_label = class_names[predicted_labels[i]]
        color = 'green' if true_label == pred_label else 'red'
        plt.xlabel(f"Actual: {true_label}\nPredicted: {pred_label}", color=color)
    plt.show()

# Visualize the first 25 images from the training set with their predictions
visualize_with_predictions(train_images, train_labels, predicted_classes)
