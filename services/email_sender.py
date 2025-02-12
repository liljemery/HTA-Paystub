import smtplib
from email.message import EmailMessage
from config.settings import settings
import os

def send_email(employees, pdf_paths):
    """Sends pay stubs via email."""
    sent_emails = []
    smtp = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    smtp.starttls()
    smtp.login(settings.EMAIL_USER, settings.EMAIL_PASS)

    for employee, pdf in zip(employees, pdf_paths):
        msg = EmailMessage()
        msg["Subject"] = "Your Paystub"
        msg["From"] = settings.EMAIL_USER
        msg["To"] = employee["email"]
        msg.set_content("Attached is your paystub.")
        
        with open(pdf, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf))

        smtp.send_message(msg)
        sent_emails.append({"email": employee["email"], "status": "sent"})
    
    smtp.quit()
    return sent_emails
