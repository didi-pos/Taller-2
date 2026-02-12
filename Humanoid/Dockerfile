FROM ubuntu:22.04

ARG ROBOT_NAME=pepper
ENV ROBOT_ENV=${ROBOT_NAME}
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    libgl1 \
    libglib2.0-0 \
    mesa-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN git clone https://github.com/0aqz0/humanoid-gym.git .

RUN sed -i "/nao_env_real/d" humanoid_gym/envs/__init__.py

# Instalar dependencias
RUN pip3 install gym==0.21.0 pybullet numpy scipy qibullet

RUN python3 - <<'EOF'
import qibullet, inspect, os
path = os.path.dirname(inspect.getfile(qibullet))
tools = os.path.join(path, "tools.py")
text = open(tools).read().replace("input(", '"y" # input(')
open(tools, "w").write(text)
EOF

# Instalar recursos de qibullet automáticamente (simular responder "y")
RUN python3 - <<'EOF'
import qibullet.tools as t
try:
    t._install_resources()
except:
    pass
EOF

RUN pip3 install -e .

ENV PYTHONPATH=/app

# Script con simulación más lenta
CMD python3 -c "import gym; import humanoid_gym; import time; env = gym.make('humanoid_gym:${ROBOT_ENV}-v0'); \
[env.step(env.action_space.sample()) or time.sleep(0.05) for _ in range(100000)]"
