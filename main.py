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
to_emails = ['marcowcorrea01@gmail.com', 'vixx2295@gmail.com']
subject = f'{data.display_name}'

html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: "Poppins", sans-serif;
            margin: 20px;
        }}
        .container {{
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            display: flex;
            align-items: center;
        }}
        .profile-image {{
            max-width: 80px;
            max-height: 80px;
            height: auto;
            border-radius: 50%;
        }}
        .info {{
            margin-top: 20px;
        }}
        .profile {{
            display: flex;
            align-items: center;
        }}
        .profile-info {{
            margin-left: 15px;
            font-size: 16px;
        }}
        .profile-name{{
            margin: 0;
            padding: 0;
            font-size: 30px;
            font-weight: 600;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="profile">
            <img src="{data.avatar}" class="profile-image" alt="Profile Image"/>
            <div class="profile-info">
                <p class="profile-name">{data.display_name}</p>
                <p>{data.description}</p>
                <p>número de posts: {data.posts_count}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

msg = MIMEMultipart('related')
msg['From'] = from_email
msg['To'] = ', '.join(to_emails)
msg['Subject'] = subject

msg.attach(MIMEText(html_body, 'html'))

if data.posts_count < 700:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')

if data.posts_count == 750:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')

if data.posts_count == 800:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')

if data.posts_count == 850:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')

if data.posts_count == 900:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')

if data.posts_count == 1000:
  try:
      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(username, password)
          server.sendmail(from_email, to_emails, msg.as_string())
      print('send!')
  except Exception as e:
      print(f'error: {e}')