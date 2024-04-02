# video-analytics-cafe-pipeless

```bash
pipeless add stream --input-uri "file:///input/demo-video-cafe.mp4" --output-uri "file:///output/demo-video-cafe-output.mp4" --frame-path "onnx-yolo"
pipeless add stream --input-uri "file:///input/demo-video-cafe.mp4" --output-uri "file:///output/demo-video-cafe-output.mp4" --frame-path "onnx-yolo,object-tracking"
pipeless add stream --input-uri "file:///input/demo-video-cafe.mp4" --output-uri "file:///output/demo-video-cafe-output.mp4" --frame-path "onnx-yolo,object-tracking,kafka"
```

```json
{
    "runtime": "onnx",
    "model_uri": "https://pipeless-public.s3.eu-west-3.amazonaws.com/yolov8n.onnx",
    "inference_params": {
        "execution_provider": "cpu"
    }
}
```