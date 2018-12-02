def load_input(filename):
    with open(filename, 'r') as input_file:
        data = [str(line.strip()) for line in input_file]

        return data

def solve_a(data):
    twos = 0
    threes = 0

    for line in data:
        _set = set(line)

        two_match = False
        three_match = False

        for char in _set:
            count = line.count(char)

            if count == 2 and not two_match:
                twos += 1
                two_match = True
            elif count == 3 and not three_match:
                threes += 1
                three_match = True

    return twos * threes

def solve_b(data):
    for line_01 in data:
        for line_02 in data:
            comp = zip(list(line_01), list(line_02))

            if sum([1 if char[0] != char[1] else 0 for char in comp]) == 1:

                return ''.join([line_01[index] if line_01[index] == line_02[index] else '' for index in range(len(line_01))])

if __name__ == '__main__':
    data = load_input('challenges/day_02/input.txt')

    assert solve_a(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']) == 12
    assert solve_b(['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']) == 'fgij'

    answer_a = solve_a(data)
    answer_b = solve_b(data)

    print(f'Part A answer: {answer_a}   Part B answer: {answer_b}')

