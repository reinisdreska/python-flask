#Lai palaistu    py -m flask run
from flask import Flask, render_template
import config
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Happy birthday, Latvia!"

@app.route("/mysql/")
def mysql():
    conn = pymysql.connect(
        host = config.host,
        user = config.user, 
        password = config.password,
        db = config.db,
        )
    
    cur = conn.cursor()
    cur.execute("SELECT  id, message,  msg_count,  server,  application,  added_at FROM reinis_test.app_errors LIMIT 10;")
    data_tuples = cur.fetchall()
    
    return render_template("/data.html", data = data_tuples)
    
    conn.close()

