def validate_password(passw):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "@#$%^&*!?"

    if len(passw)<8:
        print("Password must be at least 8 characters long.")
    else:
        for char in passw:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif char in special_characters:
                has_special = True
        if not has_upper:
            print("Password must contain at least one uppercase letter.")
        if not has_lower:
            print("Password must contain at least one lowercase letter.")
        if not has_digit:
            print("Password must contain at least one digit.")
        if not has_special:
            print("Password must contain at least one special character (ex., @#$).")
        if all([has_upper, has_lower, has_digit, has_special]):
            print("Password is valid")

def main():
    password = input("Enter a new password: ")
    validate_password(password)
if __name__ == "__main__":
    main()