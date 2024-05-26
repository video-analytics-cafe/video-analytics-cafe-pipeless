curl -X POST http://127.0.0.1:3030/streams \
     -H "Content-Type: application/json" \
     -d '{"input_uri": "file:///data/input/demo-video-cafe.mp4", "output_uri": "file:///data/output/demo-video-cafe.mp4", "frame_path": ["onnx-yolo", "object-tracking", "kafka-produc"], "restart_policy": "always"}'
     # -d '{"input_uri": "file:///data/input/demo-video-cafe.mp4", "output_uri": "file:///data/output/demo-video-cafe.mp4", "frame_path": ["onnx-yolo", "object-tracking", "kafka-produc"], "restart_policy": "always"}'
#pipeless add stream --input-uri "file:///data/input/demo-video-cafe.mp4" --output-uri "file:///data/output/demo-video-cafe.mp4" --frame-path "onnx-yolo,object-tracking,kafka-produc" --restart-policy "always"
#pipeless add stream --input-uri "http://127.0.0.1:6712/input/demo-video-cafe.mp4" --output-uri "file:///data/output/demo-video-cafe.mp4" --frame-path "onnx-yolo,object-tracking,kafka-produc" --restart-policy "always"
#pipeless add stream --input-uri "rtcp://rtsp-server:8554/stream1" --output-uri "file:///data/output/demo-video-cafe.mp4" --frame-path "onnx-yolo,object-tracking,kafka-produc" --restart-policy "always"