# ObjectDetection-Nhan_dien_bien_so_xe
This project applies Object Detection techniques to detect and extract vehicle license plates from images. It can be used in traffic surveillance systems, smart parking lots, and vehicle access control solutions.

**Features**
- Detects the position of license plates in images or video frames.
- Crops and extracts the plate region.
  
**Technologies Used**
- Python
- OpenCV
- YOLOv8
- PyTorch
- Label Studio

**How to Use**
- Train the model using your custom dataset for 50 epochs on GPU 0:
  
    results = model.train(data="my_data.yaml", epochs=50, device='0', batch = 2, imgsz = 416)  # change to your "my_data.yaml" path
  
- Predict the result:
  
  results = model.predict(r"E:\Project\Object_Detection_Biensoxe\a.png", imgsz=416)

- You do not need to use "batch = 2" and "imgsz = 416" if your GPU strong enough.

- Change the image path in "predict.py" to detect

**Example Results**
<p align="center"> <img src="results_image.png" width="600"/> </p>
