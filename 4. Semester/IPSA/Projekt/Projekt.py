#%% Imports Cell
import gzip
import time
import matplotlib.pyplot as plt

# Time_it decorator from lectures, used to time functions. 
def time_it(f):
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = f(*args, **kwargs)
        t_end = time.time()
        t = t_end - t_start
        print(f'{f.__name__} took {t:.2f} seconds')
        return result
    return wrapper

#%% Functions Cell
# Read Labels Function  
@time_it
def read_labels(filename): 
    '''
    Function to read the labes of the idx files, tests if magic number is 2049.
    Returns list of integer numbers. 
    '''
    with gzip.open(filename, "rb") as f:
        # Magic number is first 4 bytes,
        magic_number = int.from_bytes(f.read(4))
        assert magic_number == 2049, "Magic number not 2049"
        
        # Size is next 4 bytes, (not used) 
        size = int.from_bytes(f.read(4))
        
        # Return the rest of the bits in unsigned bytes. 
        return list(f.read())
    
# Read Images Function 
@time_it
def read_images(filename): 
    '''
    Function to read the idx file of images. Tests if the magic number is 2051. 
    Returns a 3D list of the images and their pixel values from 0 to 255. 
    '''
    with gzip.open(filename, "rb") as f: 
        # Magic number is first 4 bytes,
        magic_number = int.from_bytes(f.read(4))
        assert magic_number == 2051, "Magic number not 2051"
        
        # Size is next 4 bytes, (not used) 
        size = int.from_bytes(f.read(4))
        
        # Size of rows and columns 4 byte each,
        rows = int.from_bytes(f.read(4))
        columns = int.from_bytes(f.read(4))
        # Pixel values are unisigned bytes, with int value 0-255. 
        # Turn the bytes into integers, and making it an iterator
        data = iter(list(f.read()))
        
        # Makes the 3D list with list comprehension
        images = [  # Outer list comprehension (for each image)
        [  # Middle list comprehension (for each row in an image)
        [next(data) for c in range(columns)]  # Inner list comprehension (for each pixel in a column)
        for r in range(rows)
        ]
        for i in range(size)
        ]
        
    return images

# Plot images function     
def plot_images(images, labels): 
    '''
    Function for plotting images, takes a 3D list of images, and a list of their correct labels
    Plots each picture with the correct number as title. 
    '''
    for data, l in zip(images, labels): 
        plt.imshow(data, cmap='gray_r', vmin=0, vmax=255)
        plt.title(f"Number: {l}")
        plt.show()
        
    
#%% Read files Cell (30 sec)
test_labels = read_labels("mnist-master\\t10k-labels-idx1-ubyte.gz")
test_images = read_images("mnist-master\\t10k-images-idx3-ubyte.gz")

train_labels = read_labels("mnist-master\\train-labels-idx1-ubyte.gz")
train_images = read_images("mnist-master\\train-images-idx3-ubyte.gz")

#%% 1st Test Cell
print(f"Number of labels in Test Labels: {len(test_labels)}")
print(f"Test Images: \n Images: {len(test_images)} \n Rows: {len(test_images[0])} \n Col: {len(test_images[0][0])}")

# Number of pictures to plot. 
n = 1
# Plots the first n pictures in the test_images file. 
plot_images(test_images[:n], test_labels[:n])

#%% 2nd part Functions Cell
import json 

def linear_load(filename):
    '''
    Function for loading .weights as a .json file. 
    Returns 2D list of [A, b]
    '''
    with open(filename, "r") as f: 
        network = json.load(f)
        return network
        
def linear_save(filename, network): 
    '''
    Function for writing a network to a file
    Returns nothing
    '''
    with open(filename, "w") as f: 
        json.dump(network, f)
        
def image_to_vector(image): 
    '''
    Function that turns a 2D images matrix with max value 255,
    into a normalized row vector. 
    '''
    return [n/255 for rows in image for n in rows]

def add(V, U): 
    '''
    Adds to vectors
    Returns vector
    '''
    assert len(V) == len(U), f"V and U not same length, len(V)={len(V)}, len(U)={len(U)}"
    return [v+u for v, u in zip(V, U)] 

def sub(V, U): 
    '''
    Subtracts to vectors
    Returns vector
    '''
    assert len(V) == len(U), f"V and U not same length, len(V)={len(V)}, len(U)={len(U)}"
    return [v-u for v, u in zip(V, U)] 

def scalar_multiplication(scalar, V): 
    '''
    Multiplies a int or float with a vector
    Returns vector
    '''
    assert isinstance(scalar, int) or isinstance(scalar, float), "scalar is not a number"
    return [scalar * v for v in V]

def multiply(V, M): 
    '''
    Takes a list vector and a list of lists Matrix and multiplies them 
    Returns a list vector of same length as number of lists in M.
    '''
    assert len(V) == len(M), f"Multiplication not possible, len(V)={len(V)}, len(M[0])={len(M)}"
    return [sum(v * row[i] for v, row in zip(V, M))
            for i in range(len(M[0]))]   

def transpose(M):
    '''
    Takes a Matrix
    Returns the transposed matrix
    '''
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def mean_square_error(V, U):
    '''
    Calculates mean square error of two vectors of same length
    Returns Float
    '''
    assert len(V) == len(U), f"Vectors are not same length, len(V)={len(V)}, len(U)={len(U)}"
    return sum([(v-u)**2 for v,u in zip(V,U)])/len(V)

def argmax(V): 
    '''
    Takes a vector and finds the first index of the max value
    Returns int of index
    '''
    i = 0
    while V[i] != max(V):
        i += 1
    return i

def categorical(label, classes=10):
    '''
    Takes label and classes, and returns a vector of length classes, 
    where all entries are 0 except at the index label, where it is 1.
    '''
    assert isinstance(label, int)
    assert isinstance(classes, int)
    list = [0]*classes
    list[label] = 1
    return list


def predict(network, image): 
    '''
    Takes a network matrix [A, b] and a image matrix, 
    turns image into a normalized vector, 
    calculates xA+b and returns resulting vector 
    '''
    A, b = network
    x = image_to_vector(image)
    mult = multiply(x,A)
    res = add(mult,b)
    return res

@time_it
def evaluate(network, images, labels): 
    '''
    Takes a network, images and their labels,
    then runs predictions of the images using the network,
    and checks the cost and accuracy of the predictions.
    Returns tuple with list of predictions, the average cost, and the accuracy
    '''
    pre = [predict(network, image) for image in images]
    predictions = [argmax(p) for p in pre]
    Y = [categorical(l) for l in labels]
    err = [mean_square_error(p, y) for p, y in zip(pre, Y)]
    cost = sum(err)/len(err)
    acc = sum([1 if p==y else 0 for p,y in zip(predictions, labels)])/len(labels)
    return (predictions, cost, acc)

def plot_images(images, labels, prediction=False): 
    '''
    Function for plotting images, takes a 3D list of images, and a list of their correct labels
    Plots each picture with the correct number as title. 
    '''
    if prediction:
        for data, l, p in zip(images, labels, prediction):
            plt.imshow(data, cmap='gray_r', vmin=0, vmax=255)
            plt.title(f"Prediction: {l}, correct: {p}")
            plt.show()
        
    else: 
        for data, l in zip(images, labels): 
            plt.imshow(data, cmap='gray_r', vmin=0, vmax=255)
            plt.title(f"Number: {l}")
            plt.show()

# Function to display images as an animation (Just for fun)
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
def image_animation(images, labels, predictions):
    '''
    Makes animation going throug all images with their respective label and prediction
    Returns animation object
    '''
    fig, ax = plt.subplots()
    im = ax.imshow(images[0], cmap='gray_r', vmin=0, vmax=255)
    title = ax.set_title(f"Prediction: {labels[0]}, correct: {predictions[0]}")

    def update(frame):
        im.set_data(images[frame])
        title.set_text(f"Prediction: {labels[frame]}, correct: {predictions[frame]}")
        return im, title

    ani = FuncAnimation(fig, update, frames=len(images), interval=1000, repeat=True)
    plt.close(fig)
    return ani
        

#%% 2nd Test Cell 
# Tests linear_load by loading the given network file, 
# and linear_save, by saving it to a new file. 
mnist = linear_load("mnist_linear.weights")
linear_save("save_test.json", mnist)

# Image to vector test
print(f" Image to vector test, \n ", 
      f"len: {len(image_to_vector(test_images[0]))}")

# Evaluate test (Slow! - 120 sec)
eval = evaluate(mnist, test_images, test_labels)
print(f"Evaluate test \n Cost: {eval[1]}, Accuracy: {eval[2]}")

# Make animation of the first n images
n = 10
ani = image_animation(test_images[:n], test_labels[:n], eval[0][:n])
HTML(ani.to_jshtml())

#%% A visualization Cell
def reshape(V, rows, columns): 
    '''
    Takes a vector, and two integers, and then returns the 2D matrix
    with shape rows x columns
    '''
    assert isinstance(V, list), "V is not a list"
    assert isinstance(rows, int)
    assert isinstance(columns, int)
    return [V[i*columns:(i+1)*columns] for i in range(rows)]

def visualize_A(A): 
    '''
    Takes a network matrix A of shape 784 x 10, 
    visualizes the vector for each number in a subfig imshow.
    Returns figure object
    '''
    assert len(A) == 784 and len(A[0]) == 10, "Shape of A wrong"
    
    A_T = transpose(A)  # Transpose A so columns are first layer
    # Make sufig
    fig, axes = plt.subplots(2, 5, figsize=(8, 4), sharex=True, sharey=True)
    axes = axes.flatten()

    # Go through all vectors and axes, reshapes the vector, and plots the image
    for a, ax, n in zip(A_T, axes, range(10)): 
        image = reshape(a, 28, 28)
        c_int = max([abs(n) for n in a]) # For cmap range
        im = ax.imshow(image, cmap="coolwarm", vmin=-c_int, vmax=c_int)
        ax.set_title(str(n)) # Title of every number
        ax.axis('off')  # Remove ticks for cleaner look

    fig.suptitle("Visualization of A", fontsize=20) # Main title

    # Add colorbar 
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    fig.colorbar(im, cax=cbar_ax)

    # Show plot
    plt.subplots_adjust(wspace=0.1, hspace=0.1, top=0.85)
    plt.show()
    return fig

# Make the visualization of A
print("Visualization of mnist_linear.weights")        
a = visualize_A(mnist[0])


#%% 3rd Function Cell
import random 

def create_batches(values, batch_size): 
    '''
    Splits a list of values up in permuted batches
    Returns a list of batches
    '''
    assert isinstance(values, list), "Values is not a list"
    assert isinstance(batch_size, int), "batch_size not int"

    random.shuffle(values)
    return [values[i:i+batch_size] for i in range(0, len(values), batch_size)]

#@time_it # Every update is 0.3 sec
def update(network, images, labels): 
    '''
    Takes a network, a list of images and corresponding correct labels, 
    then updates the network with the given formulas. 
    Returns a new network 
    '''
    A, b = network
    n = len(images)

    for im, lab in zip(images, labels): 
        x = image_to_vector(im)
        a = add(multiply(x,A), b)
        y = categorical(lab)

        σ = 0.1 
        
        # Calculate the sums by adding dA and db for each image
        delta = scalar_multiplication(σ/n*2/10, sub(a, y))
        b = sub(b, delta)
        for j in range(len(b)): 
            for i in range(len(A)):
                A[i][j] -= x[i]*delta[j]

    return [A, b]

@time_it
def learn(images, labels, epochs, batch_size): 
    A = [[random.uniform(0, 1/784) for _ in range(10)] for _ in range(784)]
    b = [random.uniform(0, 1) for _ in range(10)]

    network = [A, b]

    for e in range(epochs): 
        t_start = time.time()

        # For each batch, the list(zip()) is so the images stays with its label when it is permuted
        for batch in create_batches(list(zip(images, labels)), batch_size):
            # Then unsips the list 
            im, lab = zip(*batch)
            network = update(network, im, lab)

        # Save after each epoch
        t_end = time.time()
        t = t_end - t_start
        print(f"\nEpoch {e+1} done took {t:.2f} seconds")
        linear_save("my_network.json", network)

    return network


#%% 3rd Test Cell
print(f"Create_batch test: \n {create_batches(list(zip([1,2,3,4], [1,2,3,4])), 2)}")


#%% Learning Cell - Learning full training takes 3 min per epoch at batch size 100
n = 1000 # Learn from n first images
network = learn(train_images[:n], train_labels[:n], 5, 100)
vis = visualize_A(network[0])
eval = evaluate(network, test_images[:n//2], test_labels[:n//2])
print(f"Evaluate test \n Cost: {eval[1]:.2f}, Accuracy: {eval[2]*100:.2f}%")