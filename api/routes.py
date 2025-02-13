from fastapi import APIRouter, UploadFile, Form, Depends, HTTPException
from api.security import authenticate_user
from services.file_processor import process_csv
from services.pdf_generator import generate_pdf
from services.email_sender import send_email
import tempfile
import os

router = APIRouter()

@router.post("/process")
async def process_paystubs(
    file: UploadFile,
    country: str = Form(default="do"),
    company_name: str = Form(...),
    credentials: str = Depends(authenticate_user)
):
    """Processes payroll data from CSV, generates PDFs, and sends emails."""
    try:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        employees = process_csv(file_path)

        pdf_paths = generate_pdf(employees, country, company_name)
        print("✅ All PDFs successfully generated.")

        email_log = send_email(employees, pdf_paths)

        return {"status": "success", "emails_sent": email_log}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
