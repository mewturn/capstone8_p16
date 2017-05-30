from PIL import Image

# Change the directory of the image file here
file = "sample.jpg"

# Opens the file and reads the data pixel by pixel, then puts each pixel into a list
im = Image.open(file)
pixels = list(im.getdata())

# Initialize variables: green pixels, non-green pixels and total pixels	
green = 0
other = 0
totalpixels = 0

# Do for each pixel in the image
# Each pixel is a 3-tuple -> pixel[0]: R-value, pixel[1]: G-value, pixel[2]: B-value
for pixel in pixels:
	if pixel[1] > pixel[0] and pixel[1] > pixel[2]:	# Green, if G-value > R-value AND G-value > B-value
		green += 1
	else:											# Not green, otherwise
		other += 1 

# Calculate total pixels in the image
totalpixels = green + other
	
# Outputs
print('Green: ' + str(green)+', Other: '+ str(other) + ', Total: ' + str(totalpixels))
print('Percentage of Green: ',(100 * green/totalpixels), '%') 