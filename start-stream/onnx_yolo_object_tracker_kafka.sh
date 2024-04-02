curl -X POST http://127.0.0.1:3033/streams \
     -H "Content-Type: application/json" \
     -d '{"input_uri": "file:///input/demo-video-cafe.mp4", "output_uri": "file:///output/demo-video-cafe-output.mp4", "frame_path": ["onnx-yolo", "object-tracking", "kafka-produc"], "restart_policy": "never"}'
