import webbrowser
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Happy birthday, Latvia!"

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == "__main__":
    open_browser();
    app.run(port=5000)