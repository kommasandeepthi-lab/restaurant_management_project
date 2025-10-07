import re

def format_phone_number(phone_number: str) -> str:
    
    try:
        if not isinstance(phone_number, str):
            raise ValueError("Phone number must be a strong.")

        digits = re.sub(r'\D', '', phone_number)

        if not digits:
            raise ValueError("Phone number contains no digits.")

        if len(digits) == 10:
            formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11 and digits.startswith('1'):

            formatted = f"+1 ( ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        elif len(digits) == 12 and digits.startswith('91'):
            formatted = f"+91 {digits[2:7]}-{digits[7:]}"
        else:
            formatted = f"+{digits}"

        return formatted

    except Exception as e:
        return f"Invalid phone number: {str(e)}"