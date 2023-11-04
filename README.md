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

Training statistics are as follows:
Epoch 1/10
1563/1563 [==============================] - 54s 34ms/step - loss: 1.5547 - accuracy: 0.4280 - val_loss: 1.2835 - val_accuracy: 0.5463
Epoch 2/10
1563/1563 [==============================] - 52s 34ms/step - loss: 1.1761 - accuracy: 0.5832 - val_loss: 1.1185 - val_accuracy: 0.6032
Epoch 3/10
1563/1563 [==============================] - 60s 38ms/step - loss: 1.0295 - accuracy: 0.6374 - val_loss: 0.9989 - val_accuracy: 0.6535
Epoch 4/10
Epoch 5/10
1563/1563 [==============================] - 53s 34ms/step - loss: 0.8707 - accuracy: 0.6952 - val_loss: 0.9168 - val_accuracy: 0.6839
Epoch 6/10
1563/1563 [==============================] - 52s 33ms/step - loss: 0.7624 - accuracy: 0.7341 - val_loss: 0.8662 - val_accuracy: 0.6984
1563/1563 [==============================] - 54s 34ms/step - loss: 0.7225 - accuracy: 0.7481 - val_loss: 0.9443 - val_accuracy: 0.6860
Epoch 9/10
1563/1563 [==============================] - 53s 34ms/step - loss: 0.6762 - accuracy: 0.7636 - val_loss: 0.8885 - val_accuracy: 0.6993
Epoch 10/10
1563/1563 [==============================] - 60s 38ms/step - loss: 0.6381 - accuracy: 0.7760 - val_loss: 0.9278 - val_accuracy: 0.6898

When evaluating the Model I obtained these results from the training
313/313 - 2s - loss: 0.9278 - accuracy: 0.6898 - 2s/epoch - 8ms/step

Test accuracy: 0.6898000240325928

## Conclusion
The accuracy of the classifcation of the images is about 68%

## Acknowledgments

- Thanks to the creators of the CIFAR-10 dataset for providing a standard benchmark for image classification.
- Thanks to TensorFlow and the Keras team for their fantastic deep learning library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

