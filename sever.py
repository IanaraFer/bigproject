from ast import Return
from Flask import Flask

App = Flask(__name__)

@App.route('/')
def index():
        Return "Hello, World!"
        
        if __name__ == '__main__':
            App.run (debug=True)
            
            