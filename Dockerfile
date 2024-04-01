FROM nvcr.io/nvidia/tensorrt:22.12-py3

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
    python3-dev python3-pip python3-venv

COPY scripts /scripts

RUN /scripts/postunpack.sh

USER 1001

RUN /scripts/install-nonroot.sh

# Allow to execute commands installed with pip + add pipeless to the path
ENV PATH="${PATH}:/.local/bin/:/${HOME}/.pipeless/" \
    LD_LIBRARY_PATH="${HOME}/.pipeless/:${LD_LIBRARY_PATH}" \
    GIT_PYTHON_REFRESH=quiet

WORKDIR /app

ENTRYPOINT ["/scripts/entrypoint.sh"]