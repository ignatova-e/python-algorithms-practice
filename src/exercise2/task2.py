def is_palindrome(number):
    if number < 0:
        return False

    original = number
    reversed_number = 0
    while number:
        reversed_number = reversed_number * 10 + number % 10
        number //= 10
    return original == reversed_number


def main():
    print(is_palindrome(int(input())))

if __name__ == "__main__":
    main()