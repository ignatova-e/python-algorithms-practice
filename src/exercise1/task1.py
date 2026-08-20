def main():
    first = map(float, input().split())
    second = map(float, input().split())
    print(sum(a * b for a, b in zip(first, second)))

if __name__ == "__main__":
    main()