def read_matrix(filename="input.txt"):
    with open(filename, encoding="utf-8") as source:
        return [list(map(int, line.split())) for line in source if line.strip()]


def component(matrix, start_row, start_column, visited):
    height, width = len(matrix), len(matrix[0])
    stack = [(start_row, start_column)]
    visited.add((start_row, start_column))
    cells = []
    while stack:
        row, column = stack.pop()
        cells.append((row, column))
        for delta_row, delta_column in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbour = row + delta_row, column + delta_column
            r, c = neighbour
            if (0 <= r < height and 0 <= c < width and matrix[r][c] == 1
                    and neighbour not in visited):
                visited.add(neighbour)
                stack.append(neighbour)
    return cells


def main():
    matrix = read_matrix()
    visited = set()
    squares = circles = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] != 1 or (row, column) in visited:
                continue
            cells = component(matrix, row, column, visited)
            rows = [cell[0] for cell in cells]
            columns = [cell[1] for cell in cells]
            side_rows = max(rows) - min(rows) + 1
            side_columns = max(columns) - min(columns) + 1
            if side_rows == side_columns and len(cells) == side_rows * side_columns:
                squares += 1
            else:
                circles += 1
    print(squares, circles)

if __name__ == "__main__":
    main()