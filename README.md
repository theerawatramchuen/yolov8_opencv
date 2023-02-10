# Installation for Window11 (or Ubuntu) with GPU. For non GPU machine pls follow comment in "yolov8-opencv.py"
(base) PS C:\Users\ramch> md project <br/>
(base) PS C:\Users\ramch> cd project <br/>
(base) PS C:\Users\ramch\project> conda create -n yolov8 python=3.9 -y <br/>
(base) PS C:\Users\ramch\project> conda activate yolov8 <br/>
(yolov8) PS C:\Users\ramch\project>git clone https://github.com/ultralytics/ultralytics <br/>
(yolov8) PS C:\Users\ramch\project>cd ultralytics <br/>
(yolov8) PS C:\Users\ramch\project>pip install -e '.[dev]' <br/><br/>

# Run yolov8-opencv.py
1. Download coco.txt <br/>
2. Download sample video file or use webcam at line 21 cap=cv2.VideoCapture('x') # x = 0 or 'vidyolov8.mp4' or your video file <br/>
3. python yolov8-opencv.py <br/>

### Installation notes: <br/>
#### How to fix "AssertionError: Torch not compiled with CUDA enabled" as below pytorch verion to enable cuda device as below test python command line (GPU only) <br/>
/>>>import torch<br/>
/>>>torch.cuda.is_available()<br/>
False<br/><br/>
```
pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
```
/>>>import torch<br/>
/>>>torch.cuda.is_available()<br/>
True<br/><br/>

#### How to fix "ImportError: DLL load failed" while importing win32api on Anaconda Windows<br/>
conda install pywin32

## Reference link
https://docs.ultralytics.com/python/ <br/>
https://youtu.be/QMBMWvn9DJc <br/>
https://github.com/freedomwebtech/yolov8-opencv-win11 <br/>
Download Sample Video File <br/>
https://mega.nz/file/8sNh0IzL#jMEYQuK7i7zyWsIvH7XMfaHDIEeWg44bdIZ56XbJLsI <br/>
