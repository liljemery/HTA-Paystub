import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(employees, country, company_name):

    pdf_dir = "paystubs"
    
    print(f"Checking if '{pdf_dir}' exists before creating PDFs...")
    print(f"Directory exists? {os.path.exists(pdf_dir)}")

    os.makedirs(pdf_dir, exist_ok=True)
    
    print(f"Directory '{pdf_dir}' created or already exists.")

    pdf_paths = []
    for employee in employees:
        pdf_path = os.path.join(pdf_dir, f"{employee['full_name'].replace(' ', '_')}.pdf")

        print(f"Generating PDF: {pdf_path}")  # ✅ Debugging Line

        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, f"Pay Stub for {employee['full_name']}")
        c.drawString(100, 730, f"Gross Salary: {employee['gross_salary']}")
        c.drawString(100, 710, f"Net Payment: {employee['net_payment']}")
        c.save()
        
        # ✅ Debugging: Confirm file creation
        if os.path.exists(pdf_path):
            print(f"✅ PDF successfully saved: {pdf_path}")
        else:
            print(f"❌ ERROR: PDF was not created: {pdf_path}")
        
        pdf_paths.append(pdf_path)
    
    return pdf_paths
