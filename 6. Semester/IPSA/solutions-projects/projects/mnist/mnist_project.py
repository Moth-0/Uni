from matplotlib import pyplot as plt
import gzip
from random import random, shuffle
import json
import math


################################################################################
# Reading MNIST data

def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big', signed=False)

def read_labels(gzip_file):
    '''Read a list of MNIST integer labels from a .gz file'''
    
    with gzip.open(gzip_file, 'rb') as f:
        magic = bytes_to_int(f.read(4))
        assert magic == 2049, gzip_file + ' not an MNIST label file'
        size = bytes_to_int(f.read(4))

        return list(f.read(size))


def read_images(gzip_file):
    '''Read a list of MNIST images from a .gz file'''

    with gzip.open(gzip_file, 'rb') as f:
        magic = bytes_to_int(f.read(4))
        assert magic == 2051, gzip_file + ' not an MNIST image file'    
        images, rows, columns = [bytes_to_int(f.read(4)) for _ in range(3)]

        return [[list(f.read(columns)) for _ in range(rows)] for _ in range(images)]


################################################################################
# Visualization of data

def plot_images(images, labels, prediction=None, rows=1, columns=None):
    '''Plot a list of MNIST images with labels as titles.
       Prediction is an optional list of predicted labels.
       If the prediction is wrong, a red colormap is used for the image.
    '''

    plt.figure('MNIST')
    N = len(images)
    if columns == None:
        columns = -(-N // rows)
    N = min(N, rows * columns)
    for i, (image, label) in enumerate(zip(images[:N], labels)):
        plt.subplot(rows, columns, i + 1)
        correct = not prediction or label == prediction[i]
        plt.xticks([])
        plt.yticks([])
        if correct:
            plt.title(label, color='black')
            plt.imshow(image, cmap='Greys')
        else:
            plt.title(f'{prediction[i]}, correct {label}', color='red')
            plt.imshow(image, cmap='Reds')
    plt.tight_layout()

###############################################################################
# Basic vector and matrix operations

def image_to_vector(image):
    '''Convert 2D image of [0, 255] integers to 1D array of [0, 1] floats.'''

    return [pixel / 255 for row in image for pixel in row]


def images_to_vectors(images):
    '''Convert multiple 2D images to 1D vectors.'''
    
    return [image_to_vector(image) for image in images]


def categorical(label, classes=10):
    '''Convert a value to categorical vector.

       Example: categorical(3) -> [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    '''

    return [1 if i == label else 0 for i in range(classes)]


def argmax(V):
    '''Return index in V with maximum entry.

       Example: argmax([6, 2, 7, 10, 5]) -> 3
    '''
    
    return max(range(len(V)), key=lambda i: V[i])


def create_batches(values, batch_size=100):
    '''Partition an iterable values into random batches.

       Example: create_batches(range(7), 3) -> [[3, 0, 1], [2, 5, 4], [6]]
    '''

    S = list(values) 
    shuffle(S)

    return [S[i:i + batch_size] for i in range(0, len(S), batch_size)]


def add(U, V):
    '''Add two 1D lists as vectors.'''

    return [u + v for u, v in zip(U, V)]


def sub(U, V):
    '''Subtract two 1D lists as vectors.'''

    return [u - v for u, v in zip(U, V)]


def scalar_multiplication(scalar, V):
    '''Multiply vector V with scalar'''

    return [scalar * v for v in V]


def transpose(M):
    '''Transpose 2D list M.'''
    
    return list(zip(*M))


def multiply(V, M):
    '''Vector-Matrix multiplication.'''

    return [sum(v * r for v, r in zip(V, row)) for row in transpose(M)]



###############################################################################
# Linear classifier

def load_network(file_name):
    '''Load network (A, b).'''

    with open(file_name) as file:
        A, b = json.load(file)
        return A, b


def save_network(network, file_name):
    '''Save network to file'''
    
    with open(file_name, 'w') as file:
        json.dump(network, file)


def predict(network, x):
    '''Compute xA + b'''

    A, b = network
    
    return add(multiply(x, A), b)


def mean(V):
    '''Compute mean of vector.'''
    
    return sum(V) / len(V)


def mean_square_error(U, V):
    '''Compute the mean square distance |U - V|^2 / len(U).'''

    return mean([(u - v) ** 2 for u, v in zip(U, V)])


def categorical_cross_entropy(U, V):
    return cross_entropy(U, soft_max(V))           


def cross_entropy(U, V):
    '''Compute cross entropy for two vectors of values in ]0, 1]'''

    return - sum(u * math.log(v) for u, v in zip(U, V))


def soft_max(U):
    '''Return vector V with V[i] = e ** U[i] / sum_j(e ** U[j])'''

    E = [math.e ** u for u in U]
    S = sum(E)
    return [e / S for e in E]


def evaluate(network, inputs, labels):
    '''Apply network to all inputs and return (predictions, cost, accuracy).
        predictions = predicted labels
        cost = sum_(input, label) |output - categorical(label)|^2
        accuracy = ratio of correct labels
    '''

    cost_function=mean_square_error
    #cost_function=categorical_cross_entropy

    outputs = [predict(network, x) for x in inputs]

    predictions = [argmax(output) for output in outputs]

    accuracy = mean([1 if l == p else 0 for l, p in zip(labels, predictions)])
        
    cost = mean([cost_function(categorical(label), output)
                for output, label in zip(outputs, labels)])

    return predictions, cost, accuracy


def visualize_weights(network):
    '''Visualize the weights for used each label class,
       i.e. one plot for each column of A.
    '''
    
    A, b = network
    W = transpose(A)

    fig = plt.figure()
    plt.suptitle('Linear classifier weights\n'
                 '(columns of weight matrix $A$ reshaped to image)')
    for digit in range(10):
        plt.subplot(2, 5, 1 + digit)
        weights = W[digit]
        img = [weights[r * 28:r * 28 + 28] for r in range(28)]
        plt.imshow(img, cmap='plasma')
        plt.title(digit)
        plt.xticks([])
        plt.yticks([])
    # Create new axes for colorbar
    fig.subplots_adjust(right=0.8)
    cbar_ax = fig.add_axes([0.85, 0.25, 0.025, 0.5])
    plt.colorbar(cax=cbar_ax)


def random_network():
    A = [[random() / 784 for _ in range(10)] for _ in range(784)]
    b = [random() for _ in range(10)]

    return (A, b)


def train_network(train_inputs, train_labels, test_inputs, test_labels,
                  batch_size=100, epochs=1, step_size=0.1):

    A, b = random_network()

    for epoch_id in range(1, epochs + 1):
      try:
        batches = create_batches(zip(train_inputs, train_labels))
        
        for batch_id, batch in enumerate(batches, start=1):
            print('Processing batch %s.%s' % (epoch_id, batch_id))
            d_A = [[0] * 10 for _ in range(784)]
            d_b = [0] * 10
            d_out = [0] * 10
            
            for x, label in batch:
                a = predict((A, b), x)
                y = categorical(label)

                # Categorial cross entropy                
                SUM = sum(math.e ** ai for ai in a)
                d_a = [math.e ** ai / SUM - yi for ai, yi in zip(a, y)]

                # Mean squared error
                d_a = scalar_multiplication(2 / len(a), sub(a, y))
                d_b = add(d_b, d_a)

                for i in range(784):
                    for j in range(10):
                        d_A[i][j] += x[i] * d_a[j]
                                                                                                                             
            scale = step_size / batch_size

            for i in range(784):
                for j in range(10):
                    A[i][j] -= scale * d_A[i][j]
            for j in range(10):
                b[j] -= scale * d_b[j]

            if batch_id % 10 == 0:
                print('Performing test evaluations')  # ~10 seconds on all test data
                predictions, cost, accuracy = evaluate((A, b), test_inputs[:1000], test_labels)
                print(f'{cost=:.4f}, {accuracy=:.4f}')
      except KeyboardInterrupt:
          if step_size > 1e-5:
              step_size /= 2
              print('New step_size =', step_size)
              continue
        
      print('Performing total evaluation')  # ~10 seconds
      predictions, cost, accuracy = evaluate((A, b), test_inputs, test_labels)
      print(f'{cost=:.4f}, {accuracy=:.4f}')

################################################################################

### TEST CODE ###

print('reading MNIST data')
train_labels = read_labels('train-labels-idx1-ubyte.gz')
train_images = read_images('train-images-idx3-ubyte.gz')
test_labels = read_labels('t10k-labels-idx1-ubyte.gz')
test_images = read_images('t10k-images-idx3-ubyte.gz')

print('creating input vectors for images')
train_inputs = images_to_vectors(train_images)
test_inputs = images_to_vectors(test_images)

network = load_network('mnist_linear.weights')

print('start training')
network = train_network(train_inputs, train_labels, test_inputs, test_labels)

predictions, cost, accuracy = evaluate(network, test_inputs, test_labels)
print(f'{cost=}, {accuracy=}')

plot_images(test_images[:25], test_labels, predictions, rows=5)
plt.show()
visualize_weights(network)
plt.show()
