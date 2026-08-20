def read_input():
    first_line = input().split()
    if len(first_line) != 2:
        raise ValueError
    amount, required_time = map(int, first_line)
    if amount <= 0 or required_time <= 0:
        raise ValueError

    machines = []
    for _ in range(amount):
        values = input().split()
        if len(values) != 3:
            raise ValueError
        machine = tuple(map(int, values))
        if any(value <= 0 for value in machine):
            raise ValueError
        machines.append(machine)
    return required_time, machines


def main():
    try:
        required_time, machines = read_input()
        best_cost = None
        for first in range(len(machines)):
            year, cost, working_time = machines[first]
            for second in range(first + 1, len(machines)):
                other_year, other_cost, other_time = machines[second]
                if year == other_year and working_time + other_time == required_time:
                    total_cost = cost + other_cost
                    if best_cost is None or total_cost < best_cost:
                        best_cost = total_cost
        if best_cost is None:
            raise ValueError
        print(best_cost)
    except (EOFError, ValueError):
        print("Invalid input")

if __name__ == "__main__":
    main()