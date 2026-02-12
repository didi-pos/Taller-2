FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar lo necesario
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Descargar el repo AQUÍ DENTRO del contenedor
WORKDIR /app
RUN git clone https://github.com/utiasDSL/gym-pybullet-drones.git .

# Instalar dependencias Python (en vez de requirements.txt)
RUN pip3 install pybullet numpy gymnasium stable-baselines3
RUN pip3 install -e .

# Ejecutar los drones
CMD ["python3", "gym_pybullet_drones/examples/pid.py"]
