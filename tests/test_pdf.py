from services.pdf_generator import generate_pdf

def test_pdf_generation(test_csv):
    """Tests if PDFs are generated correctly from payroll data."""
    employees = [
        {"full_name": "John Doe", "gross_salary": 5000, "net_payment": 4500},
        {"full_name": "Jane Smith", "gross_salary": 4000, "net_payment": 3500}
    ]
    pdf_files = generate_pdf(employees, "do", "atdev")

    assert len(pdf_files) == 2
    for pdf in pdf_files:
        assert pdf.endswith(".pdf")
