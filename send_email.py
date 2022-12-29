import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'EMAIL'
email['to'] = 'EMAIL'
email['subject'] = 'SUBJECT'

# you can use a list of names and other variables to create custom emails
email.set_content(html.substitute({'name': 'INSTERT_NAME'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('YOUR_EMAIL_ADDRES', 'GMAIL_API_KEY')
    smtp.send_message(email)
    print('all good boss!')
