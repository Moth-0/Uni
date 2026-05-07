# NEED TO USE PYTHON 3.7 TO GENERATE THE NEURAL NETWORK
# C:\Users\au121\AppData\Local\Programs\Python\Python37\python.exe ocr-mnist.py

import numpy as np
import os

layer_size = 512
network_file = f'mnist{layer_size}-linear.weights'

# A1, b1, A2, b2  = neural network 

def predict_digit(img):
    '''Given a 28 x 28 image of a handwritten digit, predicts a value 0-9'''
    
    layer1_in  = img.flatten()
    layer1_out = np.maximum(0.0, layer1_in @ A1) + b1
    layer2_out = layer1_out @ A2 + b2

    return np.argmax(layer2_out)


def read_network(filename):
    global A1, b1, A2, b2

    with open(filename) as f:
        A1, b1, A2, b2 = map(np.array, eval(f.readline()))


def create_and_save_network(filename, layer_size=512):
    # requires Python 3.7, since uses TensorFlow that does not support Python 3.8 (yet)
    # only load Keras module when this function is called
    from keras import models, layers
    from keras.datasets import mnist
    from keras.utils import to_categorical

    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    # originally 512 nodes = 98.1%, 25 nodes = 94.8% accuracy, 10 nodes = 92%, 5 nodes = 86%
    network = models.Sequential()
    network.add(layers.Dense(layer_size, activation='relu', input_shape=(28 * 28,)))
    network.add(layers.Dense(10, activation='softmax'))

    network.compile(
        optimizer='rmsprop',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    train_images = train_images.reshape((60000, 28 * 28)).astype('float32') / 255
    test_images  = test_images .reshape((10000, 28 * 28)).astype('float32') / 255

    train_labels = to_categorical(train_labels)
    test_labels  = to_categorical(test_labels)

    network.fit(train_images, train_labels, epochs=10, batch_size=128)

    test_loss, test_acc = network.evaluate(test_images, test_labels)
    print('test_acc:', test_acc)

    print('Saving neural network to', filename)
    data = [a.tolist() for a in network.get_weights()]
    with open(filename, 'w') as f:
        print(data, file=f)


# create network if not already created and save to file
if not os.path.exists(network_file):
    create_and_save_network(network_file, layer_size)

# read network from file
read_network(network_file)

