# CIFAR-10 CNN Classifier

This repository contains a set of Python scripts for training a convolutional neural network (CNN) to classify images from the CIFAR-10 dataset. The project demonstrates a complete workflow from data preprocessing to model evaluation and visualization of predictions.

## Project Structure

- `data_preprocessing.py`: Loads the CIFAR-10 dataset and performs preprocessing such as normalization.
- `model.py`: Defines the CNN architecture using TensorFlow and Keras.
- `train.py`: Trains the CNN model using the preprocessed CIFAR-10 data.
- `evaluate.py`: Evaluates the trained model's performance on the test dataset.
- `main.py`: Provides a demonstration of the model's predictions on a subset of images.
- `utils.py`: Contains utility functions for visualization of the CIFAR-10 images and model predictions.
- `cnn_model.h5`: This is the trained model.

## Getting Started

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/OkeahDavid/CIFAR-10-CNN-Classifier.git
cd CIFAR-10-CNN-Classifier
pip install -r requirements.txt
```

## Result of the Training and Evaluation of the Model
![Figure_2](https://github.com/OkeahDavid/CIFAR-10-CNN-Classifier/assets/82973470/655f1379-496c-457e-b550-1ecbc3dc1626)

## Acknowledgments

- Thanks to the creators of the CIFAR-10 dataset for providing a standard benchmark for image classification.
- Thanks to TensorFlow and the Keras team for their fantastic deep learning library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

