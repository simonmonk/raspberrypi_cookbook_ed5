import cv2
import numpy as np
from picamera2 import Picamera2
from imutils import resize

diff_threshold = 1000000

picam2 = Picamera2()
picam2.start()

def getImage():
    img = picam2.capture_array()
    img = resize(img, width=800)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (3, 3)) 
    return img

old_image = getImage()

while True:
    new_image = getImage()
    diff = cv2.absdiff(old_image, new_image)
    diff_score = np.sum(diff)
    # print(diff_score)
    if diff_score > diff_threshold:
        print("Movement detected")
    old_image = new_image