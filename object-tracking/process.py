# make stateful

from norfair import Detection, draw_points
import numpy as np


def hook(frame_data, context):
    tracker = context['tracker']
    frame = frame_data['modified']
    bboxes, scores, labels = frame_data['user_data'].values()
    norfair_detections = yolo_to_norfair(bboxes, scores, labels)
    tracked_objects = tracker.update(detections=norfair_detections)
    draw_points(frame, drawables=tracked_objects)
    frame_data['modified'] = frame
    bboxes, scores, labels, obj_track_ids = get_user_data_from_tracker(tracked_objects)
    frame_data['user_data'] = {
        "bboxes": bboxes,
        "scores": scores,
        "labels": labels,
        "obj_track_ids": obj_track_ids
    }


def get_user_data_from_tracker(tracked_objects):
    bboxes, scores, labels, obj_track_ids = [], [], [], []

    for obj in tracked_objects:
        print(f"obj.last_detection.points.reshape(-1).squeeze().tolist(): {obj.last_detection.points.reshape(-1).squeeze()}")
        bboxes.append(obj.last_detection.points.reshape(-1).squeeze().tolist())
        scores.append(float(obj.last_detection.scores[0]))
        labels.append(obj.last_detection.label)
        obj_track_ids.append(obj.id)
    return bboxes, scores, labels, obj_track_ids


def yolo_to_norfair(bboxes, scores, labels):
    norfair_detections = []
    for i, bbox in enumerate(bboxes):
        box_corners = [[bbox[0], bbox[1]], [bbox[2], bbox[3]]]
        box_corners = np.array(box_corners)
        corners_scores = np.array([scores[i], scores[i]])
        norfair_detections.append(Detection(points=box_corners, scores=corners_scores, label=labels[i]))

    return norfair_detections
