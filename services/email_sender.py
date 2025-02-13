import smtplib, ssl
from email.message import EmailMessage
from config.settings import settings

def send_email(employees, pdf_paths):
    """Sends pay stubs via Gmail SMTP with HTML content."""
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

                plain_text = f"Dear {employee['full_name']},\n\nYour paystub for the period {employee['period']} is attached.\n\nBest regards,\n{settings.COMPANY_NAME}"

                total_deductions = (
                    employee["health_discount_amount"]
                    + employee["social_discount_amount"]
                    + employee["taxes_discount_amount"]
                    + employee["other_discount_amount"]
                )

                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Your ATDev Paystub</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f8fc;
                            margin: 0;
                            padding: 0;
                        }}
                        .email-container {{
                            max-width: 600px;
                            margin: 40px auto;
                            background: #ffffff;
                            border-radius: 8px;
                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                            padding: 20px;
                            text-align: center;
                        }}
                        h1 {{
                            color: #2a72c8;
                            font-size: 22px;
                            margin-bottom: 10px;
                        }}
                        p {{
                            color: #555;
                            font-size: 16px;
                            line-height: 1.6;
                        }}
                        .paystub-info {{
                            background: #e8f1fc;
                            padding: 15px;
                            border-radius: 5px;
                            text-align: left;
                            margin: 20px 0;
                        }}
                        .paystub-info p {{
                            margin: 5px 0;
                        }}
                        .cta-button {{
                            display: inline-block;
                            padding: 12px 24px;
                            margin-top: 20px;
                            background-color: #2a72c8;
                            color: #ffffff;
                            text-decoration: none;
                            border-radius: 5px;
                            font-weight: bold;
                        }}
                        .cta-button:hover {{
                            background-color: #1e5aa8;
                        }}
                        .footer {{
                            margin-top: 30px;
                            font-size: 12px;
                            color: #777;
                        }}
                    </style>
                </head>
                <body>
                    <div class="email-container">
                        <h1>Your Paystub from {settings.COMPANY_NAME}</h1>
                        <p>Dear <strong>{employee['full_name']}</strong>,</p>
                        <p>We hope you're doing well! Your paystub for the period <strong>{employee['period']}</strong> is now available. Please find it attached to this email.</p>
                        
                        <div class="paystub-info">
                            <p><strong>Position:</strong> {employee['position']}</p>
                            <p><strong>Gross Salary:</strong> ${employee['gross_salary']}</p>
                            <p><strong>Taxes & Deductions:</strong> ${total_deductions}</p>
                            <p><strong>Net Payment:</strong> ${employee['net_payment']}</p>
                        </div>

                        <p>If you have any questions regarding your payment, please contact the HR department.</p>
                        
                        <a href="mailto:hr@atdev.com" class="cta-button">Contact HR</a>

                        <p class="footer">&copy; 2025 {settings.COMPANY_NAME} | This is an automated email, please do not reply.</p>
                    </div>
                </body>
                </html>
                """

                msg.set_content(plain_text)
                msg.add_alternative(html_content, subtype="html")

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
