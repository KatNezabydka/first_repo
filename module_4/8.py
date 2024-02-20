def is_valid_password(password):
    if not password or len(password) < 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_upper and has_lower and has_digit

    return True

password = "Password123"
if is_valid_password(password):
    print("The password is valid.")
else:
    print("The password is not valid.")