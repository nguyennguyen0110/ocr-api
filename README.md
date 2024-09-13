# OCR API


## Description
This project serving model for OCR task.


## Installation
- Install docker, vary depend on the OS, check https://docs.docker.com/engine/install/
- Build docker image (may need admin or sudo prefix), note that there is dot at the end. You can 
change the image name and version to your own need:
    
        docker build -t image_name:version .
- Run container with the image created, change docker port and app port to the actual port used:
    
        docker run -p 127.0.0.1:docker_port:app_port image_name:version


## Usage
This project is used for personal coding practice.


## Support
nguyennta@icloud.com


## Contributing
Project structure:
- README.md: this project instruction file.
- app.py: main file to run this project (Flask application is created here).
- requirements.txt: file contain the dependencies that need to install.
- Dockerfile: file used to containerize this project with docker.
- model: contain AI models, include binary file or weights file, best point file.
- service: contain service file.
- utility: contain utility file.
- route: contain file for routing.
- templates: contain html file.
- static: contain static file such as css, images.


## Authors
This project is done by nguyennta@icloud.com


## License
This is just a personal project for practice coding. It uses MMOCR and Tesseract for OCR task, so it follow 
the license of these libraries.


## Project status
- Developing
- Current host: local
