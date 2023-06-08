import sqlite3
# Connect to SQLite database
conn = sqlite3.connect('Email/emails.db')
c = conn.cursor()

subject = "CFL League 1"
sender = "LSD Presidents"
body = "Hi everyone, <br> This is going well.<br> Please do well at league tournaments, you will do well. <br> Regards, <br> Presidents of Debate"
c.execute("CREATE TABLE IF NOT EXISTS monday_briefing (subject LONGTEXT, sender LONGTEXT, body LONGTEXT)")
c.execute("CREATE TABLE IF NOT EXISTS misc (subject LONGTEXT, sender LONGTEXT, body LONGTEXT)")
c.execute("CREATE TABLE IF NOT EXISTS tournaments (subject LONGTEXT, sender LONGTEXT, body LONGTEXT)")
c.execute("REPLACE INTO monday_briefing (subject, sender, body) VALUES (?, ?, ?)", 
          (subject, sender, body))
c.execute("REPLACE INTO misc (subject, sender, body) VALUES (?, ?, ?)", 
          (subject, sender, body))
c.execute("REPLACE INTO tournaments (subject, sender, body) VALUES (?, ?, ?)", 
          (subject, sender, body))

print(body)
# Close database connection
conn.commit()
conn.close()