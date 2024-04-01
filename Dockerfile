FROM miguelaeh/pipeless:latest-tensorrt

WORKDIR /app

COPY ./onnx-yolo onnx-yolo
COPY ./object-tracking object-tracking

CMD ["pipeless", "start", "--stages-dir", "."]