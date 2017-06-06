from tkinter import *
from PIL import Image
import sys

root = Tk()

## Takes the file name as the first argument 
## ** should be .jpg file type
file = sys.argv[1]
im = Image.open(file)

## Gets the image resolutions 
width,height = im.size

## Reads the data pixel by pixel, then puts each pixel into a list
pixels = list(im.getdata())

## Puts the pixels onto the Tkinter window
def put_pixel(image, position, colour):
    r,g,b = colour  
    height,width = position
    
    # Converts hexadecimal to RGB
    image.put("#%02x%02x%02x" % (r,g,b), (width,height))

## Initializes the Tkinter window to put the pixels onto
photo = PhotoImage(width=width, height=height)

## Recreates the image in the Tkinter window 
for i in range (height):
    for j in range (width):
        put_pixel(photo, (i,j), pixels[height * i + j])

label = Label(root, image=photo)
label.grid()
root.mainloop()