import smtplib
from email.mime.text import MIMEText

EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"

def send_email(client):

    subject = "Website for your business"
    body = f"""
Hello,

I noticed your business might benefit from a modern website.

I can create a professional website quickly.

Reply YES if interested.

Regards
AI Web Agency
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = client

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, client, msg.as_string())
        server.quit()

        print(f"Email sent to {client}")

    except Exception as e:
        print("Email error:", e)
