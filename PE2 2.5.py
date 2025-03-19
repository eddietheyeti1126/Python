import re

def is_valid_password(password):
    """Checks if the password meets the required security criteria."""
    
    # Check length (8 to 20 characters)
    if not (8 <= len(password) <= 20):
        return False
    
    # Check at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check at least one number
    if not re.search(r"\d", password):
        return False

    # Check at least one special character from !@#$%&*
    if not re.search(r"[!@#$%&*.]", password):
        return False

    return True

print(is_valid_password("gB3!fKtmR1"))  # True
print(is_valid_password("Np4$uYvxm&9"))  # True
print(is_valid_password("Hello123"))  # False
print(is_valid_password("5e@9vq%#7"))  # False
print(is_valid_password("PWAJXRMQFQ"))  # False
print(is_valid_password("XwrY$&dmFt"))  # False
print(is_valid_password("lTnJXUMu7m"))  # False
print(is_valid_password("3e"))  # False
