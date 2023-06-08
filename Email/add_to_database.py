import sqlite3
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Connect to SQLite database
conn = sqlite3.connect('emails.db')
c = conn.cursor()

# Authenticate to Gmail API
creds = Credentials.from_authorized_user_file('Email/token.json')
service = build('gmail', 'v1', credentials=creds)

# Get list of emails from Gmail API
results = service.users().messages().list(userId='me', maxResults=100).execute()
messages = results.get('messages', [])

# Iterate over each email and add to appropriate table in database
for msg in messages:
    msg_id = msg['id']
    message = service.users().messages().get(userId='me', id=msg_id).execute()
    headers = message['payload']['headers']
    subject = ''
    sender = ''
    body = ''
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        elif header['name'] == 'From':
            sender = header['value']
    if 'parts' in message['payload']:
        parts = message['payload']['parts']
        for part in parts:
            if part['mimeType'] == 'text/plain':
                body = part['body']['data']
    else:
        body = message['payload']['body']['data']
    # Decode base64 encoded body
    body = base64.urlsafe_b64decode(body).decode('utf-8')
    # Add email to appropriate table in database
    if  'Monday Briefing' in subject:
        c.execute("REPLACE INTO monday_briefing (subject, sender, body) VALUES (?, ?, ?)", (subject, sender, body))
    elif  'Tournament' in subject:
        c.execute("REPLACE INTO tournaments (subject, sender, body) VALUES (?, ?, ?)", (subject, sender, body))
    else:
        c.execute("REPLACE INTO misc (subject, sender, body) VALUES (?, ?, ?)", (subject, sender, body))
    conn.commit()

# Close database connection
conn.close()