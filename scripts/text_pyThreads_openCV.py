# import libraries
import cv2
import numpy
import threading
import os
import random

path_to_file        = "temp-files/imgs/"
file_name           = "attempt{file}.png"

def workFucnt1(path_to_file, file_name):

    # creating a circle with openCV
    # set up numpy array

    img			= numpy.zeros( (512,512,3), numpy.uint8 )

    for each in range(2000):

        # format the file path
        fileName 	= file_name.format(file=each)
        randSeed    = each

        path        = path_to_file + fileName

        xPos        = int( tdu.rand(randSeed) * 512 )
        yPos        = int( tdu.rand(randSeed + 1) * 512)


        # draw a circle with openCV
        circle 		= cv2.circle(img, (xPos, yPos), 63, (0,0,255), -1)

        # save the resulting image
        cv2.imwrite(path, circle)

    return

# workFucnt1(path_to_file, file_name)

myThread            = threading.Thread(target=workFucnt1, args=(path_to_file, file_name,))
myThread.start()

