# CNN
Image classifier using tensorflow and keras

A convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that that is used for analyzing visual imagery.
This image classifier is using tensorflow and keras. OpenCV is also used in this.
OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. 

For more details and tutorials visit https://www.tensorflow.org/ for tensorflow and https://keras.io/ for keras. Visit https://opencv.org/about.html to know more about OpenCV.


After training and testing, we will save the model and then we will use that saved model to predict future results so that we do not have to retrain out model everytime we start out system.
The training and testing part is done in main.py file. The trained model is then saved by the same file. To predict the class of a new image, the main.py should be executed atleast once in the system because it will create model.json and model.h5 files that will be required by the predictor.py file.

The database that we are using can be downloaded from http://www.superdatascience.com/wp-content/uploads/2017/03/Convolutional-Neural-Networks.zip. The dataset contains a total of 10000 images, half of cats and other half of dogs. 4000 is for training and 1000 is for testing for each class.
