from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello all! This is Steve Freeland's flask for Project 2"

if __name__ == '__main__':
    app.run() 