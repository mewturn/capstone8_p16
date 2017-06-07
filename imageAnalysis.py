from PIL import Image
import sys

## Takes the file name as the first argument
file = sys.argv[1]
im = Image.open(file)

## Converts .png to .jpg if the image is in .png
## Reopens the file afterwards
if file.lower().endswith('.png'):
    rgb_im = im.convert('RGB')
    file = file[:-4] + '.jpg'
    rgb_im.save(file)
    im = Image.open(file)
    
## Reads the data pixel by pixel, then puts each pixel into a list
pixels = list(im.getdata())

## Initialize variables: green pixels, non-green pixels and total pixels	
green = 0
other = 0
totalpixels = 0

## Do for each pixel in the image
## Each pixel is a 3-tuple -> pixel[0]: R-value, pixel[1]: G-value, pixel[2]: B-value
for pixel in pixels:
    print(pixel)
    if pixel[1] > pixel[0] and pixel[1] > pixel[2]:	# Green, if G-value > R-value AND G-value > B-value
        green += 1
    else:											# Not green, otherwise
        other += 1 

## Calculate total pixels in the image
totalpixels = green + other
	
## Outputs
print('Green: ' + str(green)+', Other: '+ str(other) + ', Total: ' + str(totalpixels))
print('Percentage of Green: ',(100 * green/totalpixels), '%') 