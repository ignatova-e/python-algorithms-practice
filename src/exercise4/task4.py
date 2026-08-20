def main():
    try:
        rows = int(input())
        if rows <= 0:
            raise ValueError
    except ValueError:
        print("Natural number was expected")
        return

    current = [1]
    for _ in range(rows):
        print(*current)
        current = [1] + [current[index] + current[index + 1]
                         for index in range(len(current) - 1)] + [1]

if __name__ == "__main__":
    main()