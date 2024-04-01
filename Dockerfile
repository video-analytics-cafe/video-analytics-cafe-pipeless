FROM miguelaeh/pipeless:latest-tensorrt

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

#COPY ./onnx-yolo onnx-yolo
COPY ./yolo yolo
COPY ./object-tracking object-tracking

ENV RUST_BACKTRACE=1
ENV PIPELESS_USER_PYTHON_PACKAGES=opencv-python;numpy;ultralytics;norfair

CMD ["pipeless", "start", "--stages-dir", "."]