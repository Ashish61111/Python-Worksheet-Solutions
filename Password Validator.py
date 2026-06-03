def validate_password(password):

    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if not any(char.isupper() for char in password):
        errors.append("Password must contain at least one uppercase letter")

    if not any(char.islower() for char in password):
        errors.append("Password must contain at least one lowercase letter")

    if not any(char.isdigit() for char in password):
        errors.append("Password must contain at least one digit")

    special_characters = "!@#$%^&*"
    if not any(char in special_characters for char in password):
        errors.append("Password must contain at least one special character (!@#$%^&*)")

    is_valid = len(errors) == 0

    return {
        "is_valid": is_valid,
        "errors": errors
    }

# Test Cases

password1 = "Password123!"
password2 = "pass"
password3 = "PASSWORD123"
password4 = "Password"

print("Password 1:", validate_password(password1))
print("Password 2:", validate_password(password2))
print("Password 3:", validate_password(password3))
print("Password 4:", validate_password(password4))