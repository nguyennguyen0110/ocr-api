# Specify base image
FROM ubuntu:24.04

# Tell docker the port to use
EXPOSE 5000

# Install packages
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get install -y python3-venv && \
    apt-get install -y git && \
    apt-get install -y tesseract-ocr

# Make virtual environment for project
RUN python3 -m venv venv

# Install dependencies
COPY requirements.txt .
RUN venv/bin/pip3 install -r requirements.txt

# Copy trained model to required position
COPY model/vie_price_tag.traineddata  /usr/share/tesseract-ocr/5/tessdata/
# Copy all files from source to container directory
COPY . .

# The command to run when start docker image
CMD ["venv/bin/gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "-t", "120", "app:app"]
