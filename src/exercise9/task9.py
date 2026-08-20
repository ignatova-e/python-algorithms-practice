def main():
    degree_text, point_text = input().split()
    degree, point = int(degree_text), float(point_text)
    coefficients = [float(input()) for _ in range(degree + 1)]

    derivative = 0.0
    for index, coefficient in enumerate(coefficients[:-1]):
        power = degree - index
        derivative = derivative * point + coefficient * power
    print(f"{derivative:.3f}")

if __name__ == "__main__":
    main()