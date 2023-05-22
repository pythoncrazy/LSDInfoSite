import email
import imaplib

from email_config import gmail_pass, user, host


def read_email_from_gmail(count=3, contain_body=False):
    '''
    Returns the number of emails as 'count', in the form of a list of a list
    [0] is the person who it is from, [1] is the subject of the email, 
    [2] (if contain_body==True), is the body of the email.
    
    '''

    # Create server and login
    mail = imaplib.IMAP4_SSL(host)
    mail.login(user, gmail_pass)

    # Using SELECT to chose the e-mails.
    res, messages = mail.select('INBOX')

    # Caluclating the total number of sent Emails
    messages = int(messages[0])
    # Iterating over the sent emails
    for i in range(messages, messages - count, -1):
        print(i)
        # RFC822 protocol
        res, msg = mail.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])

                # Store the senders email
                sender = msg["From"]

                # Store subject of the email
                subject = msg["Subject"]

                # Store Body
                body = ""
                temp = msg
                if temp.is_multipart():
                    for part in temp.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip text/plain type
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            break
                else:
                    body = temp.get_payload(decode=True)

                # Print Sender, Subject, Body
                ret_list = []
                tmp = []
                tmp.append(sender)
                tmp.append(subject)
                if(contain_body):
                    tmp.append(body)
                ret_list.append(tmp)
    return ret_list

    mail.close()
    mail.logout()

x= read_email_from_gmail(3,True)
print(len(x))
print(x)