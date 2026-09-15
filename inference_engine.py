import time
import numpy as np
import cv2
import supervision as sv
from ultralytics import YOLO

class DetectionEngine:
    """
    Helper class to handle YOLOv8 object detection and Supervision tracking.
    Written for traffic video analysis.
    """
    def __init__(self, model_path="yolov8n.pt"):
        # Load pre-trained lightweight YOLO model
        self.model = YOLO(model_path)
        
        # COCO IDs for vehicles (2: car, 3: motorcycle, 5: bus, 7: truck)
        self.target_classes = [2, 3, 5, 7]
        self.class_labels = {
            2: "car",
            3: "motorcycle",
            5: "bus",
            7: "truck"
        }
        
        # ByteTrack instance to keep track of vehicle IDs across frames
        self.tracker = sv.ByteTrack(
            track_activation_threshold=0.15,
            minimum_matching_threshold=0.8,
            lost_track_buffer=30 # keep lost targets for ~30 frames
        )

    def process_frame(self, frame):
        start_time = time.time()
        
        # Run YOLO inference on current frame
        results = self.model(frame, verbose=False, conf=0.15)[0]
        
        # Convert results to Supervision format
        detections = sv.Detections.from_ultralytics(results)
        
        # Filter detections so we only care about vehicles
        if len(detections) > 0:
            valid_mask = np.isin(detections.class_id, self.target_classes)
            detections = detections[valid_mask]
            
        # Update tracker with new detections
        tracked = self.tracker.update_with_detections(detections)
        
        output_list = []
        if tracked.tracker_id is not None and len(tracked.tracker_id) > 0:
            for bbox, track_id, cls_id, conf in zip(
                tracked.xyxy, tracked.tracker_id, tracked.class_id, tracked.confidence
            ):
                output_list.append({
                    "track_id": int(track_id),
                    "class": self.class_labels.get(int(cls_id), "vehicle"),
                    "confidence": float(round(conf, 2)),
                    "bbox": [int(coord) for coord in bbox]
                })
                
        # Calculate time taken for this frame
        process_time_ms = round((time.time() - start_time) * 1000, 2)
        
        return frame, output_list, process_time_ms