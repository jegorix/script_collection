
def validate_email(email: str) -> bool:
    
    if not isinstance(email, str):
        raise TypeError("Передан неверный тип данных")
    
    if not ("@" in email and "." in email.split("@")[-1]):
        raise ValueError("Передан неверный формат email")
    
    return True


if __name__ == "__main__":
    # ✅ 1. Корректный email
    print(validate_email("user@example.com"))         # True
    print(validate_email("john.doe@domain.co.uk"))    # True

    # ❌ 2. Нет символа @
    try:
        validate_email("userexample.com")
    except ValueError as e:
        print(e)  # Передан неверный формат email

    # ❌ 3. Нет точки после @
    try:
        validate_email("user@examplecom")
    except ValueError as e:
        print(e)  # Передан неверный формат email

    # ❌ 4. Неверный тип данных
    try:
        validate_email(12345)
    except TypeError as e:
        print(e)  # Передан неверный тип данных

    # ❌ 5. Пустая строка
    try:
        validate_email("")
    except ValueError as e:
        print(e)  # Передан неверный формат email 