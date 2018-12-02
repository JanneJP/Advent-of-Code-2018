def load_input(filename):
    with open(filename, 'r') as input_file:
        data = input_file.read().strip()

        return data

def solve_a(data):
    return 0

def solve_b(data):
    return 0

if __name__ == '__main__':
    data = load_input('INSERT_PATH_HERE')

    answer_a = solve_a(data)
    answer_b = solve_b(data)

    print(f'Part A answer: {answer_a}   Part B answer: {answer_b}')
