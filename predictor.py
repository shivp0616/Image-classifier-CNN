import numpy as np
import cv2
import tensorflow as tf

global loaded_model, graph

# Load json and create model

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

from keras.models import model_from_json
loaded_model = model_from_json(loaded_model_json)

# Load weights into new model

loaded_model.load_weights("model.h5")
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
graph = tf.get_default_graph()

# Predicting the class of a new image

pred = "name_of_image.jpg"
img = cv2.imread(pred)
img = cv2.resize(img,(64,64))
img = np.reshape(img,[1,64,64,3])
with graph.as_default():        
    classes = loaded_model.predict_classes(img)
    res = ''
    if classes[0]==0:
        res = 'cat'
    else:
        res = 'dog'
    print(res)
