def validate_payroll_data(df):
    """Checks if all required fields are present in CSV."""
    required_columns = [
        "full_name", "email", "position", "health_discount_amount",
        "social_discount_amount", "taxes_discount_amount",
        "other_discount_amount", "gross_salary", "gross_payment",
        "net_payment", "period"
    ]
    return all(col in df.columns for col in required_columns)
