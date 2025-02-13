import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def generate_pdf(employees, country, company_name):
    pdf_dir = "paystubs"
    os.makedirs(pdf_dir, exist_ok=True)

    pdf_paths = []
    
    translations = {
        "do": {
            "paystub": "Comprobante de Pago",
            "gross_salary": "Salario Bruto",
            "gross_payment": "Pago Bruto",
            "net_payment": "Pago Neto",
            "health": "SFS",
            "social": "AFP",
            "taxes": "ISR",
            "others": "Otros",
        },
        "usa": {
            "paystub": "Paystub Payment",
            "gross_salary": "Gross Salary",
            "gross_payment": "Gross Payment",
            "net_payment": "Net Payment",
            "health": "Health Insurance",
            "social": "Social Security",
            "taxes": "Taxes",
            "others": "Others",
        },
    }

    lang = translations.get(country, translations["do"])

    logo_dir = "company_logos"
    logo_path = os.path.join(logo_dir, f"{company_name}.png")
    default_logo = os.path.join(logo_dir, "default.jpeg")

    for employee in employees:
        pdf_path = os.path.join(pdf_dir, f"{employee['full_name'].replace(' ', '_')}.pdf")
        c = canvas.Canvas(pdf_path, pagesize=letter)
        
        if os.path.exists(logo_path):
            logo = ImageReader(logo_path)
        else:
            logo = ImageReader(default_logo)

        c.drawImage(logo, 400, 700, width=150, height=50, preserveAspectRatio=True, mask='auto')

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, f"{lang['paystub']} - {company_name}")

        # Employee Details
        c.setFont("Helvetica", 12)
        c.drawString(100, 720, f"Employee: {employee['full_name']}")
        c.drawString(100, 700, f"Position: {employee['position']}")
        c.drawString(100, 680, f"Period: {employee['period']}")

        # Payroll Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 650, f"{lang['gross_salary']}: {employee['gross_salary']}")
        c.drawString(100, 630, f"{lang['gross_payment']}: {employee['gross_payment']}")
        c.drawString(100, 610, f"{lang['net_payment']}: {employee['net_payment']}")

        # Deductions
        c.setFont("Helvetica", 12)
        c.drawString(100, 580, f"{lang['health']}: {employee['health_discount_amount']}")
        c.drawString(100, 560, f"{lang['social']}: {employee['social_discount_amount']}")
        c.drawString(100, 540, f"{lang['taxes']}: {employee['taxes_discount_amount']}")
        c.drawString(100, 520, f"{lang['others']}: {employee['other_discount_amount']}")

        c.save()
        pdf_paths.append(pdf_path)

    return pdf_paths
