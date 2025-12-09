import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "your_email@example.com"
sender_password = "your_password" # Use App Password if 2FA is enabled
receiver_email = "recipient@example.com"
subject = "Test Email"
body = "This is a test email sent from Python."

# Create the email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    # Connect to the SMTP server (e.g., Gmail's SMTP server)
    with smtplib.SMTP_SSL('127.0.0.1', 2500) as server: # Use 465 for SSL, 587 for TLS
        server.login(sender_email, sender_password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")