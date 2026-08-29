# Developing Test Cases for a Password Validator
# Step 1: Define Requirements
# A valid password must:
# - Be at least 8 characters long
# - Contain at least one uppercase letter
# - Contain at least one digit
# Step 2: Write Test Cases First
def test_password_validator():
# Normal valid cases
    assert is_valid_password("Password123") == True
    assert is_valid_password("MyPass99") == True
# Edge cases - invalid
    assert is_valid_password("short1A") == False # Too short
    assert is_valid_password("nouppercase1") == False # No uppercase
    assert is_valid_password("NoDigits") == False # No digits
    assert is_valid_password("") == False # Empty string
    print("All password validation tests passed!")
# Step 3: Implement the Function
def is_valid_password(password):
# Check length
    if len(password) < 8:
        return False
# Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False
# Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    return has_digit
# Run tests
test_password_validator()
