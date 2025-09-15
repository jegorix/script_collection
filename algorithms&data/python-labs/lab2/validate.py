
def validate_email(email: str) -> bool:
    
    if not isinstance(email, str):
        raise TypeError("Передан неверный тип данных")
    
    if not ("@" in email and "." in email.split("@")[-1]):
        raise ValueError("Передан неверный формат email")
    
    return True