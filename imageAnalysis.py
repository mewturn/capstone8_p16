## Milton Li 2017
## Capstone 8 - Project 16: Bio-waste Disposal
## Singapore University of Technology and Design

## Analyses an image RGB values in order to train a model which recognizes "green" pixels

from PIL import Image
import sys
import numpy as np

def getPixelData(file):
    im = Image.open(file)
    ## Converts .png to .jpg if the image is in .png
    ## Reopens the file afterwards
    if file.lower().endswith(".png"):
        rgb_im = im.convert("RGB")
        file = file[:-4] + ".jpg"
        print("Converted .jpg image to .png image.")
        
        rgb_im.save(file)
        im = Image.open(file)
        
    ## Reads the data pixel by pixel, then puts each pixel into a list
    pixels = list(im.getdata())
    print("Successfully extracted image data from", file)
    return pixels

def calculateRGB(pixels):
    ## Initialize variables: green pixels, non-green pixels and total pixels	
    green = 0
    other = 0
    processedpixels = 0
    totalpixels = len(pixels)
    
    ## Completion iterator and update interval to keep track of progress
    i = 1
    interval = 10.0
    
    print("Processing...")
        
    ## Do for each pixel in the image
    ## Each pixel is a 3-tuple -> pixel[0]: R-value, pixel[1]: G-value, pixel[2]: B-value
    for pixel in pixels:      
        processedpixels += 1  
              
        ## Prepare an array of pixels and normalise w.r.t. the maximum value of RGB: 255.0
        pixelarray = np.insert(np.asarray(pixel), 0, 1)
        pixelarray = np.divide(pixelarray, 255.0)
        
        ## Current Classification Method -> w: [0.081832, -1.2328, 2.9351, -1.0643]
        weights = np.asarray([0.081832, -1.2328, 2.9351, -1.0643])
        
        ## Classifier: f(x) = w <dot> x
        score = np.dot(pixelarray, weights)
        
        ## If score is more than 1, we are confident that it is a green pixel
        if score > 1:
            green += 1
        else:
            other += 1
        
        ## Keeping track of the progress    
        if (100 * processedpixels/totalpixels >= i * interval):
            print(100 * processedpixels/totalpixels, "% complete")  
            i += 1
            
        ''' Old Classification Method 
        if pixel[1] > pixel[0] and pixel[1] > pixel[2]:	# Green, if G-value > R-value AND G-value > B-value
            green += 1
        else:											# Not green, otherwise
            other += 1 
        '''
    
    ## Green pixel ratio
    greenratio = (100 * green/totalpixels)
    
    ## Outputs
    print("Green:", green, "Non-green:", other, "Total:", totalpixels)
    print("Percentage of Green:", greenratio, "%") 
    return greenratio
    
## Runs code    
if __name__ == "__main__":
    ## Takes the file name as the first argument
    file = sys.argv[1]
    calculateRGB(getPixelData(file))    
    
    ## Data Tabulation
    ## green1.jpg -> Green: 16,622, Non-green: 1,067, Percentage of Green: 94.0%
    