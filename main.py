import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
from dotenv import load_dotenv
from atproto import Client

load_dotenv()
useremail = os.getenv('EMAIL')
passemail = os.getenv('EMAILPASSWORD')
user = os.getenv('USER')
password = os.getenv('PASSWORD')

client = Client(base_url='https://bsky.social')
client.login(user, password)

data = client.get_profile(actor='nabomgz.bsky.social')

smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = useremail
password = passemail

from_email = useremail
to_email = 'marcowcorrea01@gmail.com'
subject = 'victoria'
body = f"""
{data.display_name}
{data.description}
{data.posts_count}
{data.avatar}
"""

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(from_email, to_email, msg.as_string())
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
