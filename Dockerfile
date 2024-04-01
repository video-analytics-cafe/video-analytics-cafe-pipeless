FROM miguelaeh/pipeless:latest-tensorrt

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./onnx-yolo onnx-yolo
COPY ./object-tracking object-tracking

ENV RUST_BACKTRACE=1
ENV PIPELESS_USER_PYTHON_PACKAGES="opencv-python==4.9.0.80;numpy==1.24.4;ultralytics==8.1.41;norfair==2.2.0"

CMD ["pipeless", "start", "--stages-dir", "."]