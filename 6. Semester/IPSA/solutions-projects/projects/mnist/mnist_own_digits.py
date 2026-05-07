'''
    This file reads the image 'digits.jpg' containing 50 handwritten
    digits and applies the linear classifier (A, b) from
    'mnist_linear.weights' to the digits.
'''

#weight_file = 'mnist_linear.weights'  # generated using Keras
weight_file = 'linear_numpy.weights'  # own generated weights
picture_file = 'digits.jpg'

from PIL import Image  # Pillow module
import matplotlib.pyplot as plt
import numpy as np
import json

def rgb_to_grey(image, weights=(0.2989, 0.5870, 0.1140)):
    '''RGB to Greyscale using weights according to REC601.'''
    
    return np.sum(image * np.array(weights).reshape((1, 1, 3)), axis=2)


def negate(image, bg_threshold=0.3, variance=0.25):
    '''
       Convert greyscale (where 0 = black, 255 = white) to intensity
       Greyscale    : min -> 255, max -> 0
       bg_threshold : below -> 0
       variance     : squeze nonzero values to [(1 - variance) * 255, 255]
    '''

    image = image - np.min(image)
    image = 255 * (1 - image / np.max(image))
    mask = image < bg_threshold * np.max(image)
    image[mask] = 0
    image[~ mask] = 255 - variance * (255 - image[~ mask]) 
    
    return image


def crop(image, noise=0, threshold=128):
    '''Remove boundary columns and rows where the number of pixels
       with value < threshold is at most noise.'''
    
    height, width = image.shape
    columns = np.arange(width)[np.sum(image < threshold, axis=0) > noise]
    rows = np.arange(height)[np.sum(image < threshold, axis=1) > noise]

    return image[min(rows):max(rows) + 1, min(columns):max(columns) + 1]


def fit_square(image, side=20):
    '''Resize image to fit in a side x side square.'''
    
    height, width = image.shape
    old = max(height, width)
    h, w = height * side // old, width * side // old

    # Default resampling is BICUBIC, that can generate values outside [0, 255]
    # >>> I = Image.fromarray(np.array([[255,237,0,0]]))
    # >>> np.array(I.resize((3, 1)))
    # array([[264, 118, -14]])

    image = np.array(Image.fromarray(image).resize((w, h)))
    image[image < 0] = 0
    image[image > 255] = 255

    return image


def pad(image, side=28, threshold=128, value=0):
    '''Place image in 28 x 28 with center of mass at center'''
    
    height, width = image.shape

    row_index, col_index = np.meshgrid(np.arange(height), np.arange(width), indexing='ij')

    i = np.average(row_index[image > threshold]) 
    j = np.average(col_index[image > threshold])

    top = min(side - height, int(round(side / 2 - i)))
    left = min(side - width, int(round(side / 2 - j)))

    _image = np.full((side, side), value)
    _image[top:top + height, left:left + width] = image

    return _image


def show_grid(image, rows=5, columns=10):
    '''Visualize cutting lines'''

    height, width = image.shape[:2]
    plt.imshow(image)
    for i in range(1, columns):
        plt.plot([i * width // columns] * 2, [0, height], 'r:')
    for i in range(1, rows):
        plt.plot([0, width], [i * height // rows] * 2, 'r:')
    plt.xlim(-0.5, width - 0.5)
    plt.ylim(height - 0.5, -0.5)


def to_mnist(image):
    '''Normalize image to MNIST format.'''

    return pad(negate(fit_square(crop(image, noise=3))))


def cut(image, i, j, rows=5, columns=10):
    '''Cut cell out of grid image'''
    
    height, width = image.shape

    return image[i * height // rows:(i + 1) * height // rows,
                 j * width // columns:(j + 1) * width // columns]


def create_mnist_tests(image, rows=5, columns=10):
    '''Split image to MNIST test data: images, labels'''
 
    images = [to_mnist(cut(image, i, j, rows, columns))
              for i in range(rows)
              for j in range(columns)]
    
    labels = list(range(columns)) * rows

    return images, labels


def predict(network, image):
    '''Evaluate linear classifier'''
    
    A, b = network

    return np.argmax(image.reshape((1, 28 * 28)) @ A + b)


######################################################################


if __name__ == '__main__':
    # Load picture with 50 handwritten digits
    image = np.array(Image.open(picture_file))
    grey = rgb_to_grey(image)

    # Make image into 50 normalized MNIST test cases
    images, labels = create_mnist_tests(grey)

    # read linear classifier (A, b) from file
    A, b = map(np.array, json.load(open(weight_file)))

    # Show original image with cutting lines
    show_grid(image)
    plt.show()

    # Show predictions for the 50 digits
    plt.suptitle('Predictions by linear classifier')
    for i, (img, label) in enumerate(zip(images, labels)):
        plt.subplot(5, 10, 1 + i)
        answer = predict((A, b), img)
        ok = answer == label
        plt.imshow(img, cmap='Greys' if ok else 'Reds')
        if not ok:
            plt.title(answer, color='r')
        plt.axis('off')
    plt.show()

