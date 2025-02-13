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
        width, height = letter
        
        if os.path.exists(logo_path):
            logo = ImageReader(logo_path)
        else:
            logo = ImageReader(default_logo)
        
        c.drawImage(logo, 50, height - 100, width=150, height=50, preserveAspectRatio=True, mask='auto')
        c.setFont("Helvetica-Bold", 16)
        c.drawString(220, height - 80, f"{lang['paystub']} ({employee['period']})")
        c.setFont("Helvetica", 12)
        c.drawString(220, height - 100, employee['full_name'])
        c.drawString(220, height - 115, employee.get('position', ''))
        
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, height - 160, f"{lang['gross_salary']}")
        c.drawString(180, height - 160, f": {employee['gross_salary']}")
        c.drawString(50, height - 180, f"{lang['gross_payment']}")
        c.drawString(180, height - 180, f": {employee['gross_payment']}")
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, height - 210, f"{lang['net_payment']}")
        c.drawString(180, height - 210, f": {employee['net_payment']}")
        
        c.setFont("Helvetica-Bold", 12)
        c.drawString(350, height - 160, "Descuentos")
        c.setFont("Helvetica", 12)
        c.drawString(350, height - 180, f"{lang['social']}")
        c.drawString(450, height - 180, f": {employee['social_discount_amount']}")
        c.drawString(350, height - 200, f"{lang['health']}")
        c.drawString(450, height - 200, f": {employee['health_discount_amount']}")
        c.drawString(350, height - 220, f"{lang['taxes']}")
        c.drawString(450, height - 220, f": {employee['taxes_discount_amount']}")
        c.drawString(350, height - 240, f"{lang['others']}")
        c.drawString(450, height - 240, f": {employee['other_discount_amount']}")
        
        total_deductions = sum([
            employee['social_discount_amount'], 
            employee['health_discount_amount'], 
            employee['taxes_discount_amount'], 
            employee['other_discount_amount']
        ])
        c.setFont("Helvetica-Bold", 12)
        c.drawString(350, height - 260, "Total")
        c.drawString(450, height - 260, f": {total_deductions}")
        
        c.save()
        pdf_paths.append(pdf_path)
    
    return pdf_paths