from ultralytics import YOLO

# Load PyTorch model
model = YOLO("yolov8n.pt")

# Export to ONNX format (simplified for optimal edge parsing)
model.export(format="onnx", simplify=True)
print("Model successfully exported to yolov8n.onnx")