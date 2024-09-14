def validate(password):
    errors = []
    if not 6<len(password)<10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    if sum(char.isdigit() for char in password) < 2:
        errors.append("Password must have at least 2 digits")
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")

u_password = input()
validate(u_password)