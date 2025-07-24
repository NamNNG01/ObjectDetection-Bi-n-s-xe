from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")  # model nhanh nhất

    results = model.train(
        data="my_data.yaml",  # đường dẫn tới YAML
        epochs=50,  # hoặc ít hơn nếu chỉ test
        imgsz=416,  # nhỏ hơn = nhanh hơn
        batch=32,  # tận dụng GPU tối đa
        device='0',  # GPU
        workers=2,  # tránh nghẽn CPU nếu máy yếu
        augment=False,  # tắt tăng cường dữ liệu
        verbose=False,  # không in log
        save=False,  # không lưu mỗi epoch
        name="ultrafast_train"  # tên phiên train
    )


