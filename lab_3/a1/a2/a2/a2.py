import string
password = input("Enter password")
errors = []
allowed_chars = string.ascii_letters + string.digits + "*-#"
if len(password) != 8:
    errors.append("password need be 8 symbols")
if not any(c.isupper() for c in password):
    errors.append("no one capslk letter")
if not any(c.islower() for c in password):
    errors.append("no one undercapslk letter")
if not any(c.isdigit() for c in password):
    errors.append("no one number")
if not any(c in "*-#" for c in password):
    errors.append("no one special symbols")
if not all(c in allowed_chars for c in password):
    errors.append("special symbols *-#")
if not errors:
    print("good password")
else:
    for error in errors:
        print(error)
