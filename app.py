from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


def get_db_connection(path):
    conn = sqlite3.connect(path +'.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/hello_world')
def hello():
    return 'Hello, World!'

@app.route('/emails')
def render_email_main():
    return render_template("emails.html")

@app.route('/tournaments')
def render_tournaments():
    conn = get_db_connection("Email/emails")
    tournament_info = conn.execute('SELECT * FROM tournaments').fetchall()
    conn.close()
    return render_template("tournaments.html", tournament_info = tournament_info)

@app.route('/monday_briefing')
def render_monday_briefings():
    conn = get_db_connection("Email/emails")
    monday_briefings = conn.execute('SELECT * FROM monday_briefing').fetchall()
    conn.close()
    return render_template("monday_briefings.html", monday_briefings = monday_briefings)

@app.route('/misc')
def render_misc():
    conn = get_db_connection("Email/emails")
    misc = conn.execute('SELECT * FROM misc').fetchall()
    conn.close()
    print(misc)
    for i in misc["body"]:
        i.replace("\\n","\n")
    return render_template("misc.html", misc = misc)