import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('emails.db')
c = conn.cursor()



# Create table for Monday Briefing emails
c.execute('''CREATE TABLE IF NOT EXISTS monday_briefing
             (id INTEGER PRIMARY KEY, subject TEXT, sender TEXT, body TEXT)''')

# Create table for Monday Briefing emails
c.execute('''CREATE TABLE IF NOT EXISTS tournaments
             (id INTEGER PRIMARY KEY, subject TEXT, sender TEXT, body TEXT)''')

# Create table for misc emails
c.execute('''CREATE TABLE IF NOT EXISTS misc
             (id INTEGER PRIMARY KEY, subject TEXT, sender TEXT, body TEXT)''')