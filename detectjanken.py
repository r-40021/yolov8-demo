from ultralytics import YOLO
model = YOLO("best-200images-20batch.pt")
results = model(0 , show=True)