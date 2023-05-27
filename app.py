from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello_world')
def hello():
    return 'Hello, World!'

@app.route('/emails')
def render_email_main():
    return render_template("emails.html")

@app.route('/tournament')
def render_tournament():
    return render_template("tournament.html")

@app.route('/monday_briefing')
def render_monday_briefings():
    return render_template("monday_briefings.html")

@app.route('/misc')
def render_misc():
    return render_template("misc.html")