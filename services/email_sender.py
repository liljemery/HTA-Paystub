import smtplib, ssl
from email.message import EmailMessage
from config.settings import settings

def send_email(employees, pdf_paths):
    """Sends pay stubs via Gmail SMTP."""
    sent_emails = []

    try:
        context = ssl._create_unverified_context()
        with smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT, context=context) as smtp:
            smtp.login(settings.EMAIL_USER, settings.EMAIL_PASS)

            for employee, pdf in zip(employees, pdf_paths):
                msg = EmailMessage()
                msg["Subject"] = "Your Paystub"
                msg["From"] = settings.EMAIL_USER
                msg["To"] = employee["email"]
                msg.set_content("Attached is your paystub.")

                with open(pdf, "rb") as f:
                    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=pdf)

                smtp.send_message(msg)
                sent_emails.append({"email": employee["email"], "status": "sent"})

        return sent_emails

    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Authentication failed: {e}")
        return {"error": "Authentication failed. Check your App Password or enable SMTP access."}

    except smtplib.SMTPException as e:
        print(f"❌ SMTP error: {e}")
        return {"error": f"SMTP error: {str(e)}"}

    except Exception as e:
        print(f"❌ General error: {e}")
        return {"error": str(e)}
