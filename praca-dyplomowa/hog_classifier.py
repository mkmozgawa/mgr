import numpy as np
import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import dlib

image_colour = mpimg.imread('path_to_image.jpg') # load the image
image_gray = cv2.cvtColor(image_colour, cv2.COLOR_BGR2GRAY) # grayscale conversion
detector = dlib.get_frontal_face_detector() # load the classifier
faces = detector(image_gray, 0) # search for all potential faces in the grayscale image

res = image_colour.copy() # create a copy of the original image (to draw on it later)

for face in faces:
    # for each detected face, draw a green bounding box around it
    cv2.rectangle(res, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

cv2.imwrite('output.jpg', cv2.cvtColor(res, cv2.COLOR_BGR2RGB)) # save results
