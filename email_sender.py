import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Amal Kuriakose'
email['to'] = 'amalkuriakose802@gmail.com'
email['subject'] = 'Test with Python'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('youremail@gmail.com', 'yourpassword')
    smtp.send_message(email)
    print('Mail sent')