import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
# video1 = r'C:\Apps\Masters_SJSU\Prof_Stas_ISA\Ball Boy\video_ball_track\data\video\Pexels Videos 992693.mp4'



# Inference
results = model(img)
# res = model(video1)
# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
