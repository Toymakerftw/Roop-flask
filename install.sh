#!/bin/bash

# Create a virtual environment
python3 -m venv roop_env

# Activate the virtual environment
source roop_env/bin/activate

# Clone the repository
git clone https://github.com/OMGSAMUELRBR/roop-unlock
cd roop-unlock

# Checkout to the specific commit
git checkout 1f8409eebfb5c9009e48b32dcd8bd88a7fb4d2b8

# Install the required packages
pip install onnxruntime-gpu && pip install -r requirements.txt

# Download the required model
wget https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx

# Deactivate the virtual environment
deactivate
