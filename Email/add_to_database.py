import sqlite3
con = sqlite3.connect("emails.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS mondaybrief(year, subject, body)") 
cur.execute("CREATE TABLE IF NOT EXISTS tournamentemail(year, subject, body)")
cur.execute("CREATE TABLE IF NOT EXISTS misc(year, subject, body)")
cur.execute("""
    INSERT INTO mondaybrief VALUES
        (2023, "Monday Briefing #26", )
""")