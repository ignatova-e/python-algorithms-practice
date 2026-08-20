def parse_number(value):
    value = value.strip()
    if not value:
        raise ValueError

    sign = 1
    if value[0] in "+-":
        sign = -1 if value[0] == "-" else 1
        value = value[1:]

    parts = value.split(".")
    if len(parts) > 2 or not any(parts) or any(
            part and not part.isdigit() for part in parts):
        raise ValueError
    if len(parts) == 1:
        integer_part, fractional_part = parts[0], ""
    else:
        integer_part, fractional_part = parts
    if not integer_part and not fractional_part:
        raise ValueError
    if not integer_part and not fractional_part:
        raise ValueError

    number = 0
    for digit in integer_part:
        number = number * 10 + ord(digit) - ord("0")
    factor = 0.1
    for digit in fractional_part:
        number += (ord(digit) - ord("0")) * factor
        factor /= 10
    return sign * number


def main():
    try:
        print(f"{parse_number(input()) * 2:.3f}")
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()