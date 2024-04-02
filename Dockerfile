#FROM nvcr.io/nvidia/tensorrt:24.02-py3
FROM nvcr.io/nvidia/tensorrt:22.12-py3
#FROM nvcr.io/nvidia/deepstream:6.4-gc-triton-devel

COPY scripts/install_packages /usr/bin/install_packages

# Install required pacakges
RUN install_packages \
    wget ca-certificates curl git \
    # Gstreamer
    libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
    libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools \
    gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 gstreamer1.0-pulseaudio gstreamer1.0-rtsp \
    # Gstreamer deps
    libcairo2-dev libgirepository1.0-dev \
    # Python
    python3-dev python3-pip python3-venv python3

COPY scripts /scripts

RUN /scripts/postunpack.sh

USER 1001

RUN /scripts/install-nonroot.sh

USER root

# Allow to execute commands installed with pip + add pipeless to the path
ENV PATH="${PATH}:/.local/bin/:/${HOME}/.pipeless/" \
    LD_LIBRARY_PATH="${HOME}/.pipeless/:${LD_LIBRARY_PATH}" \
    GIT_PYTHON_REFRESH=quiet

WORKDIR /app
ENV NVIDIA_DRIVER_CAPABILITIES video,compute,graphics,utility
ENV NVIDIA_VISIBLE_DEVICES all
#ENV NVIDIA_VISIBLE_DEVICES nvidia.com/gpu=all
ENV GST_DEBUG=3
#ENV CUDA_VER=12.3
#ENV CUDA_VER=11.8
#ENV CUDA_HOME=/usr/local/cuda-${CUDA_VER}
#ENV CFLAGS="-I$CUDA_HOME/include $CFLAGS"
#ENV PATH=${CUDA_HOME}/bin:${PATH}
#ENV LD_LIBRARY_PATH=${CUDA_HOME}/lib64:${LD_LIBRARY_PATH}
#ENV LD_LIBRARY_PATH=/usr/lib:/usr/local/lib:$LD_LIBRARY_PATH

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./yolo yolo
#COPY ./onnx-yolo onnx-yolo
COPY ./object-tracking object-tracking

ENTRYPOINT ["/scripts/entrypoint.sh"]