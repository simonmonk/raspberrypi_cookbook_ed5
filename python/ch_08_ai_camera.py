from ai_camera import IMX500Detector
import time

model = "/usr/share/imx500-models/imx500_network_ssd_mobilenetv2_fpnlite_320x320_pp.rpk"
camera = IMX500Detector(model_path=model)

camera.start(show_preview=True)

while True:
    detections = camera.get_detections()
    labels = camera.get_labels()

    if detections is not None:
        for detection in detections:
            label_index = int(detection.category)
            if  label_index < len(labels): # sometimes index is higher than number of labels
                label = labels[int(detection.category)]
                confidence = detection.conf
                if label == "person" and confidence > 0.4:
                    print(f"Person detected with {confidence:.2f} confidence!")

    time.sleep(0.1)