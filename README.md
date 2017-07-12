# Capstone Project 16 Bio-waste Disposal
This repository contains the essential codes to be used for the Capstone project.

## Background and Introduction
Uses a simple regression model with a quadratic loss function to train the colour recognition weights in order to determine the proportion of surface area of a container which is covered by duckweed. The image data is captured by a Raspberry Pi camera module, and subsequently processed through an image analysis process, using the weights trained from the training datasets.

## trainingData.py
Contains the training model which is used to learn the weights and determine whether each pixel in an image is "green" or "non-green". 
Requires the use of imageAnalysis.py.

## imageAnalysis.py
Processes the image and contains a function to convert .png to .jpg format where RGB values can be extracted from each pixel and processed accordingly.

## putPixel.py
Visualise the classified data based on the classifier weights and threshold confidence values. 
Uses Tkinter PhotoImage and plots points classified as "green" for a visual inspection.

## cameraCapture.py
Capture an image using Raspberry Pi at a regular interval.

## raspberry_gpio.py
Read and write output to and from Raspberry Pi's GPIO pins.

## txt_to_csv.py
Converts the .txt file output of the spectrophotometer into a .csv file format which can be used for further processing and visualisation in R.

## plot_Abs_Wavelength.R
Plots light absorbance values against light wavelengths.