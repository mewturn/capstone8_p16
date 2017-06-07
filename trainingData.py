from PIL import Image
import sys
import numpy as np
from time import sleep
from math import exp

# Requires imageAnalysis.py
from imageAnalysis import getPixelData

## totalimages: number of total images
## type: type of image -> "green" or "notgreen"
def run(totalimages, type):
    ## Output to be returned at the end
    output = []
    
    ## Gets the pixel data from the image
    for i in range(1, totalimages+1):
        image = type + str(i) + ".jpg"
        pixels = getPixelData(image)
            
        ## Adds it to the array of green output
        for pixel in pixels:
            if pixel in output:
                continue
            output.append(pixel)
    
    return output

def train(trainingdata, weights, ground_truth):   
    ## Learning rate and the expected change to last (w(t+1) - w(t))
    lr = 0.05
    eps = 0.000001
    
    ## Initialize a temporary variable to check if the expected stepsize is reached
    change = 1
    
    ## Sets the iteration count and the maximum iterations allowed
    iteration = 0
    maxitr = 2000   
    
    ## Normalise the training data w.r.t to maximum RGB value of 255
    trainingdata = np.divide(trainingdata, 255.0)
    
    ## Keep changing weights until the required step size (eps)
    while change > eps:      
    
        ## Initialise error and update term
        error = 0
        update = 0
        
        ## Keeps track of iteration number and allows us to know that the program has not hung
        iteration += 1
        
        ## The size of data: N
        N = len(trainingdata)
        
        ## Modify the weights according to the classifications
        for i in range(N):            
            predict = activation(trainingdata[i], weights)
            error += (computeError(ground_truth[i], predict)) / N
            update += (computeGradient(ground_truth[i], predict, trainingdata[i])) / N                      
        
            weights -= lr * update
            change = np.linalg.norm(update)
          
        print("Iteration #", iteration, "Error:", error, "Weight:", weights)
        
        ## End when the expected step size is achieved (eps) or when the maximum iteration is reached    
        if iteration > maxitr:
            print("Maximum iteration reached. Error:", error)
            break
            
    print("Algorithm terminated. Optimal weights were found with error:", error)   
    print("Last change", change)
    return weights


def test(testingdata, weights, ground_truth):    
    ## Initialise error
    error = 0
    
    for data in testingdata:
        predict = activation(testingdata[i], weights)
        error += computeError(predict, ground_truth[i])
    
    return error
    
## Activation function used to predict y from w and x
def activation(parameters, weights):    
    return np.dot(parameters, weights)

## We use quadratic loss function (f(x) - y)^2 with the normalisation_term being the total number of points sampled
def computeError(actual, predict):
    return (actual - predict) ** 2

## We compute gradient of the error function w.r.t. w: (np.dot(w,x) - y) times x
def computeGradient(actual, predict, parameters):    
    print(2 * (actual - predict) * parameters)
    return 2 * (actual - predict) * parameters
    
    
## Generates a list of ground truths comprising 1 (green) or -1 (not green)
def groundTruth(ones, negs):
    truth = [1] * ones
    false = [-1] * negs
    
    return truth + false
    
if __name__ == "__main__":
    ## __images: number of images in the training set
    ## __output: Output list to write into, without duplicate RGB values
    greenimages = 1     ## Currently up to 4
    otherimages = 1     ## Currently up to 3
    greenoutput = run(greenimages, "green")
    otheroutput = run(otherimages, "notgreen")
    
    ## Training data set formed by merging the two lists
    trainingset = np.asarray(greenoutput + otheroutput)
    
    ## Adds a weight bias term 1 to the front of each x vector
    trainingset = np.insert(trainingset, 0, 1, axis=1)
        
    ## Ground truths
    groundtruths = groundTruth(len(greenoutput), len(otheroutput))
    
    # WEIGHT TRAINING
    ## Initialise weights to be [w(0), w(1), w(2), w(3)] = [0, 0, 0, 0]
    w = np.zeros(4)
    '''
    ## After 5,000 iterations: w: [-36.987, -0.387, 0.275, -0.281]
    w = np.asarray([-36.987, -0.387, 0.275, -0.281])
    
    
    ## After 10,000 iterations: w: [-65.377, -0.267, 0.379, -0.388]
    w = np.asarray([-65.377, -0.267, 0.379, -0.388])
    '''
    ## Commence training
    w = train(trainingset, w, groundtruths)
    