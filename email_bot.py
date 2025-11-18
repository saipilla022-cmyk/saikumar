import smtplib
from email.mime.text import MIMEText

EMAIL_TO = "saipilla022@gmail.com"
EMAIL_FROM = ".com"
EMAIL_PASSWORD = ""  # Gmail App Password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_issue_email(issue_key, summary):
    subject = f"New Jira Issue Created: {issue_key}"
    body = f"A new Jira issue has been created.\n\nKey: {issue_key}\nSummary: {summary}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    s.starttls()
    s.login(EMAIL_FROM, EMAIL_PASSWORD)
    s.sendmail(EMAIL_FROM, [EMAIL_TO], msg.as_string())
    s.quit()

print("Email script executed.")
