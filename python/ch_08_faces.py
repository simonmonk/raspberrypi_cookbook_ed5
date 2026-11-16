import cv2  

img = cv2.imread('faces.jpg')
height, width, _ = img.shape

face_detector = cv2.FaceDetectorYN.create(
    model="face_detection_yunet_2023mar.onnx",
    config="",
    input_size=(width, height),
    score_threshold=0.9,  # Minimum confidence score (0.0 to 1.0)
    nms_threshold=0.3,    # Non-maximum suppression threshold
    top_k=5000            # Maximum number of detections before NMS
)

_, faces = face_detector.detect(img)
print(faces)

for face in faces:
    x, y, w, h = map(int, face[:4])
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
