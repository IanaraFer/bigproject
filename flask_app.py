import sys
sys.path.append("/home/Ianarafer/bigproject")
from flask import Flask, jsonify
from bookDAO import BookDAO  # ✅ Correct reference
app = Flask(__name__)
book_dao = BookDAO()  # ✅ Initialize the instance
@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(book_dao.getAll())  # ✅ Correct usage


if __name__ == '__main__':
    app.run(debug=True, port=5005)  # ✅ Runs Flask on a different port if needed


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([{"title": "Test Book", "author": "John Doe"}])  # ✅ Hardcoded test data
