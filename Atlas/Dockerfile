FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    libgl1-mesa-glx \
    xvfb \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN git clone https://github.com/erwincoumans/pybullet_robots.git .

RUN pip3 install pybullet numpy

# Ejecutar demo de Atlas
CMD ["python3", "atlas.py"]
