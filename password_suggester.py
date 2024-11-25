import random
import string

def check_password_strength(password):

    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter."

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter."

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."

    if not any(c in string.punctuation for c in password):
        return False, "Password must contain at least one special character."
        
    return True, "Strong password."



def suggest_strong_password():
    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )
    return ''.join(random.choice(chars) for _ in range(12))



user_password = input("Enter a password to check: ")
is_strong, message = check_password_strength(user_password)

if is_strong:
    print("Password is strong.")
else:
    print(f"Weak password: {message}")
    print("Suggested strong password:", suggest_strong_password())