from flask import Flask, render_template
from route.read_text import read_text_bp
from route.demo import demo_bp


app = Flask(__name__)
app.register_blueprint(read_text_bp, url_prefix='/api')
app.register_blueprint(demo_bp, url_prefix='/demo-read-text')


@app.route(rule='/')
def root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()


# docker build -t read_text:v0.0.2 .
# docker run -p 127.0.0.1:8000:5000 read_text:v0.0.2
# docker update --restart always container_name
# docker inspect -f "{{ .HostConfig.RestartPolicy }}" container_name

# This command to use docker without the need of sudo (add current user to docker group)
# May need to create docker group first
# May need to log out and log back in to take effect
# sudo gpasswd -a $USER docker
