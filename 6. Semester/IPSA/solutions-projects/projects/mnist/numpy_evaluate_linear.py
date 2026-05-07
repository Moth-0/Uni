import numpy as np
from tensorflow import keras
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
A, b = map(np.array, eval(open('mnist_linear.weights').read()))
images, labels = test_images, test_labels
#images, labels = train_images, train_labels
outputs = (images.reshape((images.shape[0], 28 * 28)) / 255) @ A + b

predictions = np.argmax(outputs, axis=1)

categorical =  np.array(np.arange(10).reshape(1, 10) == labels.reshape(len(labels), 1), dtype=np.float64)
accuracy = np.sum(predictions == labels) / labels.size
loss = np.sum((outputs - categorical) ** 2) / outputs.size

print('Accuracy:', accuracy)
print('Loss:', loss)
