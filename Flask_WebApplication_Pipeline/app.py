from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return "Welcome to the home Page"

@app.route("/contact")
def ContactUs():
    return "This is our contact Page"

@app.route("/about")
def AboutUs():
    return "This is our About Page"


if __name__ == '__main__':
    app.run(host='0.0.0.0')