import pandas as pd
from utils.validation import validate_payroll_data

def process_csv(file_path: str):
    """Reads CSV, validates data, and returns employee records."""
    df = pd.read_csv(file_path)
    if not validate_payroll_data(df):
        raise ValueError("Invalid payroll data format.")
    
    employees = df.to_dict(orient="records")
    return employees
