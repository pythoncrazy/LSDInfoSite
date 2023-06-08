import sqlite3
conn = sqlite3.connect('Email/emails.db')
c = conn.cursor()



subject = "Monday Briefing #15"
sender = "Spirit Committee"
body = 'Heyo,<br><br> Hope everyone enjoyed the last league tournament of the year or the very last league for seniors :(. <br>We have a few announcements for this upcoming week<br><br> CFL Congress<br><br> <ul> <li>It is in-person at Palo Alto High School</li> <li>Check in time is 9:30 am for both competitors and judges</li> <li>Ask your VPs for more info </li> </ul> Other <ul> <li>Sign up for in-class performances here <a href="https://docs.google.com/spreadsheets/d/1Y9KeS6mnYGjdffKxv23QkXgLcnZkqwfR3bp6bJrIGT0/edit#gid=0"> Sign-Up</a> </li> </ul> That is all for this week, please let us know if you have any questions,<br> Slayyyyyyyyyyyyyyyyyyyy,<br> LSD Spirit <3'
c.execute("REPLACE INTO monday_briefing (subject, sender, body) VALUES (?, ?, ?)", 
          (subject, sender, body))
print(body)
# Close database connection
conn.commit()
conn.close()