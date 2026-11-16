import cv2
from picamera2 import Picamera2
from imutils import resize

picam2 = Picamera2()
picam2.start()

old_count = 0

try:
    while True:
        img = picam2.capture_array()
        img = resize(img, width=800)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img, (3, 3)) 

        detected_circles = cv2.HoughCircles(img,  
            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
            param2 = 60, minRadius = 15, maxRadius = 100)
        count = 0
        if detected_circles is not None:
            count = len(detected_circles[0])
        if count != old_count:
            print(count)
            old_count = count
        cv2.waitKey(100)
except:
    picam2.stop()
