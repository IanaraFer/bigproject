from ast import Return
from flask import Flask

App = Flask(__name__)

@App.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    App.run(debug=True)

