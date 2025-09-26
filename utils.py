import re
def is_valid_email(email: str) -> bool:

    if not isinstance(email, str):
        return False

    pattern = r'[a-zA-z0-9_.+-]+@[a-zA-z0-9-]'
    return bool(re,match(pattern, email))