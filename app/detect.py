

from ultralytics import YOLO

model = YOLO("last.pt")  # Đặt đúng tên file .pt bạn có

def detect_plate(image_path, output_path="static/output.jpg"):
    results = model(image_path)
    results[0].save(filename=output_path)
