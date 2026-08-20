def main():
    amount = int(input())
    numbers = {int(input()) for _ in range(amount)}
    print(len(numbers))

if __name__ == "__main__":
    main()