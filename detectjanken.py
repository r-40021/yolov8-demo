from ultralytics import YOLO
model = YOLO("best.pt")
results = model(0 , show=True)