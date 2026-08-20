def main():
    rows, columns = map(int, input().split())
    best = [0] * columns
    for row in range(rows):
        values = list(map(int, input().split()))
        for column, value in enumerate(values):
            from_above = best[column]
            from_left = best[column - 1] if column else 0
            best[column] = value + (max(from_above, from_left)
                                    if row or column else 0)
    print(best[-1])

if __name__ == "__main__":
    main()