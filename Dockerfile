# Use an official Python runtime as a parent image
FROM python:3.10-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install onnxruntime-gpu and any other needed dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install onnxruntime-gpu && pip install --no-cache-dir -r requirements.txt

# Download the required model
RUN wget https://huggingface.co/ezioruan/inswapper_128.onnx/resolve/main/inswapper_128.onnx

# Make port 5000 available to the world outside this container
EXPOSE 7777

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python3", "./run.py"]
