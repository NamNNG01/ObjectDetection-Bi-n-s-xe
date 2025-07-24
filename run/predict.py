from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLO model (change the path to your model)
model = YOLO(r"C:\Users\ADMIN\Desktop\Object Detection - biển số xe\ObjectDetection-Nhan_dien_bien_so_xe\run\runs\detect\ultrafast_train3\weights\last.pt")

results = model.predict(r"C:\Users\ADMIN\Desktop\Object Detection - biển số xe\ObjectDetection-Nhan_dien_bien_so_xe\a.png", imgsz=416)

# Print the results
for r in results:
    print(r.boxes)  # Print the bounding boxes
    im_array = r.plot()  # PLot a BRG numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1]) #RGB PIL Image
    im.show()
    im.save("results_image.png")

print(model.names)

