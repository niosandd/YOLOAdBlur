from ultralytics import YOLO
import cv2

# ------------------------------------
# [Train]
# ------------------------------------


# model = YOLO(r"D:\DataScience\Work\advertising_blurring\models\yolov8n.pt")  # загрузите предварительно обученную модель YOLOv8n
#
# model.train(data=r"D:\DataScience\Work\advertising_blurring\yolo\coco-yolo.yaml", epochs=1)


# ------------------------------------
# [Predict]
# ------------------------------------
#
# model = YOLO(r'D:\DataScience\Work\advertising_blurring\models\server\best.pt')
#
# model.predict(r'D:\DataScience\Work\advertising_blurring\dataset\outputtttt\v1\frame_90.png', save=True, imgsz=320, conf=0.5)