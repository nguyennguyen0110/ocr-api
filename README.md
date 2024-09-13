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


## Object define
**Response Object**

        {
            "code": integer - similar to html code,
            "message": string,
            "data": vary depend on which service is called
        }


## Usage
1. "/"
    - GET: html home page.
2. "/demo-read-text"
    - GET: html page to upload image.
    - POST: upload image and get text from response.
3. "/api"
    - POST:
        - Request: None
        - Response "data": a welcome message.
4. "/api/read-text"
    - POST:
        - Request: send with content type "multipart/form-data"
        
                "image": image file to read text
        - Response "data":
        
                {
                    "texts": list of read text,
                    "decoded_texts": list of read text decoded (remove accents)
                }


## Support
nguyennta@icloud.com


## Contributing
Project structure:
- model: contain AI models, include binary file or weights file, best point file.
- route: contain file for routing.
- service: contain service file.
- static: contain static file such as css, images.
- templates: contain html file.
- utility: contain utility file.
- app.py: main file to run this project (Flask application is created here).
- Dockerfile: file used to containerize this project with docker.
- README.md: this project instruction file.
- requirements.txt: file contain the dependencies that need to install.


## Authors
This project is done by nguyennta@icloud.com


## License
This is just a personal project for practice coding. It uses Tesseract for OCR task, so it follow 
the license of Tesseract.


## Project status
- Finished
- Current host: local
