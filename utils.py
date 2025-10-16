def format_currency(amount):
    return f"${amount: .2f}"

if __name__ == "__main__":
    print(format_currency(22.5))
    print(format_currency(100))