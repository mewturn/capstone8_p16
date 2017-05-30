from picamera import PiCamera
import time

camera = PiCamera()

# Initialises the file count
count = 1

# Change this to change picture-taking interval (in seconds)
t = 60

while True:
	# Output File Name (Month, Day, Hour, Minute both in 2 digits)
	filename = str(time.strftime("%m%d%H%M"))+ "file" + str(count) + ".jpg"
	
	# Capture image and save to file
	time.sleep(5)
	camera.capture(filename)
	print("Image captured to: " + filename)
	count += 1
	
	# Sleep for t seconds before taking next picture
	time.sleep(t)
	