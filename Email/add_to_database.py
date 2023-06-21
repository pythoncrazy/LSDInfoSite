import csv
import imaplib
import email
import quopri

# Connect to your email account via IMAP
imap_server = "outlook.office365.com"
username = "lelandsdin@outlook.com"
password = "curly55!!"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, password)
imap.select("INBOX")

# Search for emails with a specific subject
status, messages = imap.search(None, "SUBJECT", "Monday")
message_ids = messages[0].split(b" ")

# Save email data as CSV
with open("emails.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["sender", "subject", "body"])
    for message_id in message_ids:
        status, data = imap.fetch(message_id, "(RFC822)")
        message = email.message_from_bytes(data[0][1])
        sender = message["From"]
        subject = message["Subject"]
        html_body = None

        # Search for the HTML part of the email message
        for part in message.walk():
            if part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                break

        if html_body:
            decoded_body = quopri.decodestring(html_body).decode("utf-8")
        else:
            decoded_body = ""

        writer.writerow([sender, subject, decoded_body])

imap.close()
imap.logout()