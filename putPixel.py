## Milton Li 2017
## Capstone 8 - Project 16: Bio-waste Disposal
## Singapore University of Technology and Design

## Uses Tkinter PhotoImage to visualise pixels as a way to verify the accuracy of training using linear regression
## See trainingData.py for the simple linear regression training method

from tkinter import *
from PIL import Image
import sys
import numpy as np

## Puts the pixels onto the Tkinter PhotoImage
def put_pixel(image, position, colour):
    r,g,b = colour  
    height,width = position
    
    # Converts hexadecimal to RGB
    image.put("#%02x%02x%02x" % (r,g,b), (width,height))

## Recreates the image in the Tkinter PhotoImage 
def process_image(photo, height, width, pixels):
    print("Processing image...")
    print("Image height:", height, "Image width:", width, "Total pixels:", len(pixels))
    x = height
    y = width
    totalpixels = height*width
    processedpixels = 0
    
    ## Completion iterator and update interval to keep track of progress
    itr = 1
    interval = 10.0
    
    ## If the width is less than the height, we invert the indices to prevent an out of range error
    if width < height:
        x = width
        y = height
    
    for i in range(x):
        for j in range(y):
            #print("Processing", processedpixels, "out of", x * y, "pixels.")
            rgb = pixels[x * i + j]
            
            ## Keeping track of the progress    
            if (100 * processedpixels/totalpixels >= itr * interval):
                print(100 * processedpixels/totalpixels, "% complete")  
                itr += 1
            
            ## Creating an array of pixels: [1, r, g, b] and normalise it w.r.t. max RGB value of 255
            pixelarray = np.insert(np.asarray(rgb), 0, 1)
            pixelarray = np.divide(pixelarray, 255.0)
            
            ## Current Classification Method -> w(itr#10000): [0.081832, -1.2328, 2.9351, -1.0643]
            weights = np.asarray([0.081832, -1.2328, 2.9351, -1.0643])
            
            ## Using f(x) = w <dot> x
            score = np.dot(pixelarray, weights)
            #print (rgb, score)
            
            ## If f(x) > 1, we are confident that it is classified correctly as "green"
            if score > 1:
                put_pixel(photo, (i,j), rgb)
        
            processedpixels += 1
        
    return processedpixels
 
## Runs code
if __name__ == "__main__":
    root = Tk()
    
    ## Takes the file name as the first argument 
    ## ** should be .jpg file type
    file = sys.argv[1]
    im = Image.open(file)

    ## Gets the image resolutions 
    width,height = im.size

    ## Reads the data pixel by pixel, then puts each pixel into a list
    pixels = list(im.getdata())
     
    ## Initializes the Tkinter PhotoImage to put the pixels onto
    photo = PhotoImage(width=width, height=height)
    print("Total pixels:", height*width, "Processed pixels:", process_image(photo, height, width, pixels))

    label = Label(root, image=photo)
    label.grid()
    root.mainloop()