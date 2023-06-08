from flask import Flask, render_template
import sqlite3


app = Flask(__name__)

def get_db_connection_better(path):
    conn = sqlite3.connect(path +'.db')
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
    conn = get_db_connection_better("Email/emails")
    tournaments = conn.execute('SELECT * FROM tournaments').fetchall()
    tournaments_list = []
    for m in list(tournaments):
        tournaments_list.append(list(m))
    tournaments = tournaments_list
    return render_template("extend_emails.html", emails = tournaments_list)

@app.route('/monday_briefing')
def render_monday_briefings():
    conn = get_db_connection_better("Email/emails")
    monday_briefing = conn.execute('SELECT * FROM monday_briefing').fetchall()
    monday_briefing_list = []
    for m in list(monday_briefing):
        monday_briefing_list.append(list(m))
    monday_briefing = monday_briefing_list
    return render_template("extend_emails.html", emails = monday_briefing)

@app.route('/misc')
def render_misc():
    conn = get_db_connection_better("Email/emails")
    misc = conn.execute('SELECT * FROM misc').fetchall()
    misc_list = []
    for m in list(misc):
        misc_list.append(list(m))
    misc = misc_list
    print(misc)
    return render_template("extend_emails.html", emails = misc)