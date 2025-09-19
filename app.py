from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Returns a simple greeting string."""
    return "Hello, Jenkins!"

# This block allows running the app directly with 'python app.py'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
