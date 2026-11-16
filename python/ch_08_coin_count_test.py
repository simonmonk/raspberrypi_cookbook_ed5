import cv2
from picamera2 import Picamera2
from imutils import resize

picam2 = Picamera2()
picam2.start()

try:
    while True:
        img = picam2.capture_array()
        img = resize(img, width=800)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img, (3, 3)) 

        detected_circles = cv2.HoughCircles(img,  
            cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
            param2 = 60, minRadius = 15, maxRadius = 100)

        if detected_circles is not None:
            print(detected_circles)
            for pt in detected_circles[0]: 
                a, b, r = pt[0], pt[1], pt[2] 
                cv2.circle(img, (int(a), int(b)), int(r), 
                    (0, 255, 0), 5) 

        cv2.imshow('image', img)
        cv2.waitKey(100)
except:
    picam2.stop()
    cv2.destroyAllWindows()
