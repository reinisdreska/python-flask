#Lai palaistu    py -m flask run
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Happy birthday, Latvia!"