## Milton Li 2017
## Capstone 8 - Project 16: Bio-waste Disposal
## Singapore University of Technology and Design

## Uses simple linear regression to determine if a pixel is green or non-green

from PIL import Image
import sys
import numpy as np
from time import sleep
from math import exp

# Requires imageAnalysis.py
from imageAnalysis import getPixelData

## totalimages: number of total images
## type: type of image -> "green" or "notgreen"
def run(totalimages, type=None):
    ## Output to be returned at the end
    output = []        
    count = 0
    
    ## Gets the pixel data from the image
    for i in range(1, totalimages+1):
        image = type + str(i) + ".jpg"
        pixels = getPixelData(image)
        print("Processing image...")
        
        ## Adds it to the array of green output
        for pixel in pixels:
            if pixel in output:
                continue
                
            output.append(pixel)
        print("Complete!")
    return output

def train(trainingdata, weights, ground_truth, testingdata, test_ground_truth):   
    ## Learning rate and the expected change to last (w(t+1) - w(t))
    lr = 0.005
    eps = 1e-6
    
    ## Initialize a temporary variable to check if the expected stepsize is reached
    change = 1
    
    ## Sets the iteration count and the maximum iterations allowed
    iteration = 0
    maxitr = 10000   
    
    ## Normalise the datasets w.r.t to maximum RGB value of 255
    trainingdata = np.divide(trainingdata, 255.0)
    testingdata = np.divide(testingdata, 255.0)
    
    ## N: the size of training data
    N = len(trainingdata)
    
    ## Keep changing weights until the required step size (eps)
    while change > eps:      
    
        ## Initialise error and update term
        error = 0
        update = 0
        
        ## Keeps track of iteration number and allows us to know that the program has not hung
        iteration += 1

        ## Modify the weights according to the classifications
        for i in range(N):         
            ## Predict f(x)
            predict = activation(trainingdata[i], weights)
            
            ## Compute error for the particular x in the training data
            error += (computeError(ground_truth[i], predict)) / N
            
            ## Compute gradient for the particular x in the training data w.r.t. w
            update += (computeGradient(ground_truth[i], predict, trainingdata[i])) / N                      
        
        ## Update weights
        weights -= lr * update
        
        ## Calculate norm(w(t+1) - w(t)) 
        change = np.linalg.norm(lr * update)
          
        ## Intervals to checkpoint 
        if iteration % 200 == 0:
            print("Iteration #", iteration, "Error:", error, "Weight:", weights)            
            ## Check validation error with some set of testing data
            #print("Validation error:", test(testingdata, weights, test_ground_truth))
        
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
    N = len(testingdata)
    
    for i in range(N):
        predict = activation(testingdata[i], weights)
        error += computeError(ground_truth[i], predict)
    
    return error
    
## Activation function used to predict y from w and x
def activation(parameters, weights):    
    return np.dot(parameters, weights)

## We use quadratic loss function (f(x) - y)^2 with the normalisation_term being the total number of points sampled
def computeError(actual, predict):
    return (actual - predict) ** 2

## We compute gradient of the error function w.r.t. w: (np.dot(w,x) - y) times x
def computeGradient(actual, predict, parameters):    
    return -2 * (actual - predict) * parameters
    
    
## Generates a list of ground truths comprising 1 (green) or -1 (not green)
def groundTruth(ones, negs):
    truth = [1] * ones
    false = [-1] * negs
    
    return truth + false
    
if __name__ == "__main__":
    ## __images: number of images in the training set
    ## __output: Output list to write into, without duplicate RGB values
    greenimages = 5     ## Currently up to 5
    otherimages = 5     ## Currently up to 5
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

    '''    WEIGHTS AT DIFFERENT ITERATION NUMBERS (INTERVALS OF 2000)  
    ## ITR 2000 ->  Error: 0.29987, Weights: [0.027571, 0.10667, 1.7119, -0.15630]
    ## ITR 4000 ->  Error: 0.24196, Weights: [0.043756, -0.34832, 2.1669, -0.55597]
    ## ITR 6000 ->  Error: 0.21088, Weights: [0.057828, -0.70851, 2.5007, -0.81439]
    ## ITR 8000 ->  Error: 0.19369, Weights: [0.070381, -0.99738, 2.74890, -0.97368]
    ## ITR 10000 -> Error: 0.18378, Weights: [0.081832, -1.2328, 2.9351, -1.0643]
    '''
    
    ## WEIGHT TESTING
    testingoutput = getPixelData("test_green.jpg")
    
    ## Creates an array of testing data and adds a weight bias term 1 to the front of each x vector
    testingset = np.asarray(testingoutput)
    testingset = np.insert(testingset, 0, 1, axis=1)   
    
    ## Ground truths of test data
    testgroundtruths = groundTruth(len(testingoutput), 0)
    
    ## Commence training
    w = train(trainingset, w, groundtruths, testingset, testgroundtruths)
    