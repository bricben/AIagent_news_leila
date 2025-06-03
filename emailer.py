import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def format_email(summaries):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('email_template.html')
    return template.render(summaries=summaries)

def send_email(subject, html_body, recipient):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = recipient
    msg.attach(MIMEText(html_body, 'html'))

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, recipient, msg.as_string())