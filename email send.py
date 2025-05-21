import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Mailendo SMTP credentials
SMTP_SERVER = "smtp.mailendo.com"
SMTP_PORT = 587
SMTP_USERNAME = "bf35190a-1ae3-4c84-ae08-6a5e7c06c6b4"  # Your API Key
SMTP_PASSWORD = "40f3a627-ab32-4a94-ac65-8ca3e3fff75d"  # Your API Secret

FROM_EMAIL = "sales@jaspervalebooks.com"
TO_EMAIL = "ryanmatthewcoupe01@gmail.com"

# Load HTML email content
with open("email-template.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Construct the email message
msg = MIMEMultipart('alternative')
msg['Subject'] = "Three Days Hollow - A Story Your Church Won’t Forget"
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg.attach(MIMEText(html_content, 'html'))

# Send email using TLS
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("SMTP connection failed:", e)
