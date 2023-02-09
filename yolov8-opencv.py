# https://docs.ultralytics.com/python/
# https://youtu.be/QMBMWvn9DJc
# https://github.com/freedomwebtech/yolov8-opencv-win11
#
import cv2
import numpy as np
import torch
import pandas as pd
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def RGB(event, x,y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :
        colorsBGR = [x,y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture(0) #'vidyolov8.mp4'

my_file = open("coco.txt","r")
data = my_file.read()
class_list = data.split("\n")
print(class_list)
count=0
while True:
    ret,frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    results=model.predict(frame)
    # print(results)
    a=results[0].boxes.boxes                      # For machine without GPU 
    #a=torch.Tensor.cpu(results[0].boxes.boxes)   # For machine with GPU such as Jetson Nano
    px=pd.DataFrame(a).astype("float")
    for index,row in px.iterrows():
        # print(row)
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.putText(frame,str(c),(x1+2,y1-10),cv2.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

exit()
