from flask import Flask
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

app = Flask(__name__)

@app.route('/')
def homePage():
    return f"Welcome to the Home Page! <br/> My HostName is {hostname} <br/> My Ip Address is {IPAddr}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')