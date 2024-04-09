curl -X POST http://127.0.0.1:3030/streams \
     -H "Content-Type: application/json" \
     -d '{"input_uri": "file:///input/demo-video-cafe.mp4", "output_uri": "rtcp://localhost:7004", "frame_path": ["onnx-yolo"], "restart_policy": "never"}'
