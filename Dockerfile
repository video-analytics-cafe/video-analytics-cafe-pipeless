FROM miguelaeh/pipeless:latest-tensorrt

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./onnx-yolo onnx-yolo
COPY ./object-tracking object-tracking

ENV RUST_BACKTRACE=1

CMD ["pipeless", "start", "--stages-dir", "."]