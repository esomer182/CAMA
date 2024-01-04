import smtplib
import json

def send_email(email_data):
    from_email = ''  # Replace with email address
    password = ""  # Replace with email password

    to_email = email_data['to_email']
    subject = email_data['subject']
    message = email_data['message']

    try:
        server = smtplib.SMTP() # Use whatever SMTP port you want.
        server.starttls()
        server.login(from_email, password)
        body = f'Subject: {subject}\n\n{message}'
        server.sendmail(from_email, to_email, body)
        print(f"Email sent to {to_email} with subject: {subject}")
        server.quit()
    except Exception as e:
        print(f"Email to {to_email} failed with error: {e}")

with open('emails.json', 'r') as json_file:
    email_data_list = json.load(json_file)

for email_data in email_data_list:
    send_email(email_data)
