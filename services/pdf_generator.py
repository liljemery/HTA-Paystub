from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf(employees, country, company_name):
    """Creates pay stub PDFs for employees and saves them locally."""
    pdf_paths = []
    for employee in employees:
        pdf_path = f"paystubs/{employee['full_name'].replace(' ', '_')}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, f"Pay Stub for {employee['full_name']}")
        c.drawString(100, 730, f"Gross Salary: {employee['gross_salary']}")
        c.drawString(100, 710, f"Net Payment: {employee['net_payment']}")
        c.save()
        pdf_paths.append(pdf_path)
    return pdf_paths
