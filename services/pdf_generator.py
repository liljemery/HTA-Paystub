import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from utils.translation import translations

def generate_pdf(employees, country, company_name):
    pdf_dir = "paystubs"
    os.makedirs(pdf_dir, exist_ok=True)

    pdf_paths = []
    
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

        # Header with Logo
        c.drawImage(logo, 50, 730, width=150, height=50, preserveAspectRatio=True, mask='auto')
        c.setFont("Helvetica-Bold", 16)
        c.drawString(250, 750, f"{lang['paystub']} ({employee['period']})")
        c.setFont("Helvetica", 12)
        c.drawString(250, 735, employee['full_name'])
        c.drawString(250, 720, employee.get('position', ''))
        
        # Payroll Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, 690, f"{lang['gross_salary']}: {employee['gross_salary']}")
        c.drawString(50, 670, f"{lang['gross_payment']}: {employee['gross_payment']}")
        
        # Net Payment
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, 640, f"{lang['net_payment']}: {employee['net_payment']}")
        
        # Deductions Table
        c.setFont("Helvetica-Bold", 12)
        c.drawString(300, 690, "Descuentos")
        c.setFont("Helvetica", 12)
        c.drawString(300, 670, f"{lang['social']}: {employee['social_discount_amount']}")
        c.drawString(300, 650, f"{lang['health']}: {employee['health_discount_amount']}")
        c.drawString(300, 630, f"{lang['taxes']}: {employee['taxes_discount_amount']}")
        c.drawString(300, 610, f"{lang['others']}: {employee['other_discount_amount']}")
        
        # Total Deductions Calculation
        total_deductions = sum([
            employee['social_discount_amount'], 
            employee['health_discount_amount'], 
            employee['taxes_discount_amount'], 
            employee['other_discount_amount']
        ])
        c.setFont("Helvetica-Bold", 12)
        c.drawString(300, 590, f"Total: {total_deductions}")
        
        c.save()
        pdf_paths.append(pdf_path)
    
    return pdf_paths
