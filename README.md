# Setup

conda create -n genesis python=3.10

conda activate genesis

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128

git clone https://github.com/Genesis-Embodied-AI/Genesis.git

cd Genesis

pip install -e ".[dev]"

sudo apt-get install freeglut3 freeglut3-dev
pip install PyOpenGL PyOpenGL_accelerate

sudo apt install mesa-utils

glxinfo | grep "OpenGL vendor"
OpenGL vendor string: Intel

sudo prime-select nvidia
sudo reboot

glxinfo | grep "OpenGL vendor"
OpenGL vendor string: NVIDIA Corporation



