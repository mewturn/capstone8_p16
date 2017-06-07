from tkinter import *
from PIL import Image
import sys

root = Tk()
cv = Canvas(root)

## Takes the file name as the first argument 
## ** should be .jpg file type
file = sys.argv[1]
im = Image.open(file)

## Gets the image resolutions 
width,height = im.size

## Reads the data pixel by pixel, then puts each pixel into a list
pixels = list(im.getdata())

## Puts the pixels onto the Tkinter PhotoImage
def put_pixel(image, position, colour):
    r,g,b = colour  
    height,width = position
    
    # Converts hexadecimal to RGB
    image.put("#%02x%02x%02x" % (r,g,b), (width,height))

## Recreates the image in the Tkinter PhotoImage 
def process_image(photo, height, width, pixels):
    print(height, width, len(pixels))
    x = height
    y = width
    
    processedPixels = 0
    
    ## If the width is less than the height, we invert the indices to prevent an out of range error
    if width < height:
        x = width
        y = height
    
    for i in range(x):
        for j in range(y):
            print(x * i + j, "out of", x * y, "pixels.")
            rgb = pixels[x * i + j]
            
            if rgb[1] > rgb[0] and rgb[1] > rgb[2]:  
                put_pixel(photo, (i,j), rgb)
                
        processedPixels += j+1
        
    return processedPixels
        
## Initializes the Tkinter PhotoImage to put the pixels onto
photo = PhotoImage(width=width, height=height)
print("Total pixels:", height*width, "Processed pixels:", process_image(photo, height, width, pixels))

label = Label(root, image=photo)
label.grid()
root.mainloop()