# Capstone Project 16 Bio-waste Disposal
This repository contains the essential codes to be used for the Capstone project.

## Background and Introduction
We use a simple regression model with a quadratic loss function to train the colour recognition weights in order to determine the proportion of surface area of a container which is covered by duckweed. The image data is captured by a Raspberry Pi camera module, and subsequently processed through an image analysis process, using the weights trained from the training datasets.

## trainingData.py
This file contains the training model which is used to learn the weights and determine whether each pixel in an image is "green" or "non-green". It requires the use of imageAnalysis.py.

## imageAnalysis.py
This file helps to process the image and contains a function to convert .png to .jpg format where RGB values can be extracted from each pixel and processed accordingly.

## putPixel.py
This file allows for a visualisation of the classified data based on the classifier weights and threshold confidence values. It uses Tkinter PhotoImage and plots points classified as "green" for a visual inspection.

## cameraCapture.py
Simple code to capture an image using Raspberry Pi at a regular interval.

## raspberry_gpio.py
Simple code to read and write output to and from Raspberry Pi's GPIO pins.
