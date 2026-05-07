import gzip
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import keyboard
import json

step_size = 0.1  # for gradient descend
batch_size = 100  # size of batches used for updating the weights
network_file = 'linear_numpy.weights'  # save min cost network here

class IDX:
    '''Generic reader to read MNIST IDX files into NumPy arrays'''
    
    types = {  # IDX types -> NumPy dtypes
        0x08: 'uint8',
        0x09: 'int8',
        0x0B: 'int16',
        0x0C: 'int32',
        0x0D: 'float32',
        0x0E: 'float64'
    }

    def read_file(filename):
        '''Read a .gz file containing IDX data'''
        
        with gzip.open(filename, 'rb') as file:
            def read_uint(bytes):
                return int.from_bytes(file.read(bytes), byteorder='big', signed=False)
                
            zero, data_type, dimensions = read_uint(2), read_uint(1), read_uint(1)
            assert zero == 0 and data_type in IDX.types and dimensions > 0
            dtype = IDX.types[data_type]
            shape = tuple(read_uint(4) for _ in range(dimensions))

            return np.frombuffer(file.read(), dtype=dtype).reshape(shape)

    def read_files(*filenames):
        '''Read multiple .gz files containing IDX data'''

        return [IDX.read_file(filename) for filename in filenames]

    def mnist():
        '''Read the 4 MNIST data files'''

        return IDX.read_files(
            'train-images-idx3-ubyte.gz',
            'train-labels-idx1-ubyte.gz',
            't10k-images-idx3-ubyte.gz',
            't10k-labels-idx1-ubyte.gz'
        )


def to_categorical(label, classes=10):
    '''MNIST digit recognition.ipynb'''

    categorical = np.zeros(classes)
    categorical[label] = 1
    return categorical


class Visualizer:
    '''
       Class to Visualize dynamic weights of a linear classifier for
       MNIST data. 
    '''
    
    def __init__(self, network, accuracies, costs, history=200):
        '''
           Initialize a pyplot figure with the dynamic data to be
           visualized:
             * network = (A, b) is a linear classifier
             * accuracies = list of measured accuracies
             * costs = corresponding measured costs
           The number of recent accuracy and cost measures shown is
           determined by history.
        '''
        
        self.network = network
        self.accuracies = accuracies
        self.costs = costs
        self.history = history

        # weight plots
        A, b = network
        self.weight_plots = []
        for i in range(10):
            plt.subplot(4, 5, 1 + i)
            im = plt.imshow(A[:, i].reshape((28, 28)), cmap='plasma')
            self.weight_plots.append(im)
            plt.title(i)
            plt.xticks([])
            plt.yticks([])
        # colorbar
        cax = plt.axes([0.08, 0.55, 0.02, 0.3])
        cbar = plt.colorbar(cax=cax)
        cbar.set_ticks([])

        # accuracy plot
        self.accuracy_ax = plt.subplot(4, 1, 3)
        self.accuracy_ax.tick_params(labelbottom=False)
        plt.ylim(0, 1)
        plt.ylabel('accuracy')
        self.accuracy_best, = plt.plot([], [], 'r--')
        self.accuracy_plot, = plt.plot([], [])
        self.max_text = plt.text(0, 0, '', color='r', ha='center')

        # cost plot
        self.cost_ax = plt.subplot(4, 1, 4, sharex=self.accuracy_ax)
        plt.xlim(0, self.history)
        plt.ylim(0, 10)
        plt.ylabel('cost')
        plt.xlabel('network updates')
        self.cost_plot, = plt.plot([], [])

        
    def update(self):
        '''Update axes in plots with current network data.'''
        
        fig.suptitle(f'Batch size {batch_size}, '
                     f'step_size {step_size:.2e}, '
                     f'{len(self.accuracies)} updates, '
                     f'{epoch} epochs\n'
                     'Linear classifier weights\n'
                     '(columns of weight matrix $A$ reshaped to image)'
                     )
        # Update weight plots
        A, b = self.network
        for i, im in enumerate(self.weight_plots):
            image = A[:, i].reshape((28, 28))
            im.set_clim(np.min(A), np.max(A))
            im.set_data(image)

        # Update accuracy plot
        best_accuracy = max(self.accuracies)
        acc = accuracies[-self.history:]
        left = len(self.accuracies) - len(acc)
        right = max(self.history, len(self.accuracies))
        xs = range(left, left  + len(acc))
        self.accuracy_ax.set_xlim(left, right)
        self.max_text.set_position(((left + right) // 2, best_accuracy + 0.05))
        self.max_text.set_text(f'{best_accuracy:.3f}')
        self.accuracy_plot.set_data(xs, acc)
        self.accuracy_best.set_data([left, right], [best_accuracy] * 2)

        # Update cost plot
        self.cost_ax.set_xlim(left, right)
        self.cost_ax.set_ylim(0, max(1, max(self.costs[-self.history:])))
        self.cost_plot.set_data(xs, self.costs[-self.history:])


class Network:
    '''Implementation of a linear classifier (A, b).'''
    
    def __init__(self):
        '''Initialize network with uniform weights.'''
        
        A = np.random.random((784, 10)) / 784
        b = np.random.random((1, 10))

        self.network = A, b
    
    def predict(self, image):
        '''Predict output vector for image.'''

        A, b = self.network
        return image @ A + b

    def update(self, images, labels):
        '''Perform one backpropagation w.r.t. one batch of images.'''

        A, b = self.network
        
        d_b = np.zeros(b.shape)
        d_A = np.zeros(A.shape)

        for image, label in zip(images, labels):
            a = self.predict(image)

            # Gradient computation
            d_a = 2 / 10 * (a - to_categorical(label))
            d_b += d_a
            d_A += image.T @ d_a

        A -= d_A * step_size / batch_size # remember minus...
        b -= d_b * step_size / batch_size
      
    def evaluate(self, images, labels):
        '''Return (cost, accuracy) wrt. a set of test images.'''
        
        n = len(images)
        cost = 0.0
        accuracy = 0

        for image, label in zip(images, labels):
            prediction = self.predict(image)
            cost += np.sum((prediction - to_categorical(label)) ** 2)
            if np.argmax(prediction) == label:
                accuracy += 1

        return cost / n, accuracy /n


######################################################################


def step(frame):
    '''Main learning function called by FuncAnimation. For each call
       applies one update to the network.
    '''

    if not batches:
        global epoch
        epoch += 1

        # Create new round of batches
        idx = np.random.permutation(len(train_images))
        for idx_start in range(0, len(idx), batch_size):
            S = idx[idx_start:idx_start + batch_size]
            images = [train_images[i] for i in S]
            labels = [train_labels[i] for i in S]
            batches.append((images, labels))

    (images, labels) = batches.pop()

    cost, accuracy = LC.evaluate(test_images, test_labels)
    accuracies.append(accuracy)
    costs.append(cost)
    LC.update(images, labels)
    viz.update()

    # Periodically save best network
    global save_network, save_delay
    if cost < min(costs[:-1], default=cost):
        save_network = (LC.network[0].tolist(), LC.network[1].tolist())
    if save_delay:
        save_delay -= 1
    if save_network and save_delay == 0:
        print('saving', network_file)
        with open(network_file, 'w') as f:
            json.dump(save_network, f)
        save_network = None
        save_delay = 10
        
# Initialize learning

LC = Network()  # Initialize a linear classifier

batches = []    # Queue of batches [(images, labels), (images, labels), ...]
accuracies = [] # historic accuracies
costs = []      # historic costs
epoch = 0       # Current epoch (#times batches has been refilled)
save_delay = 10 # Number of iterations before next save possible
save_network = None  # Network to save when save_delay == 0

train_images, train_labels, test_images, test_labels = IDX.mnist()

# convert images to 1D arrays of floats in [0.0, 1.0]
train_images = train_images.reshape((60000, 1, 28 * 28)) / 255  
test_images = test_images.reshape((10000, 1, 28 * 28)) / 255

# Allow step_size to be inc-/decreased during runtime with F2/F1
def update_step_size(factor):
    global step_size
    step_size *= factor
    
keyboard.add_hotkey('F1', lambda: update_step_size(0.5))
keyboard.add_hotkey('F2', lambda: update_step_size(2))

# Initialize visualization 
fig = plt.figure()
viz = Visualizer(LC.network, accuracies, costs, history=200)
ani = FuncAnimation(fig, step)

# Show visualization & start updating network
plt.show()
