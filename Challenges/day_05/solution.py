def load_input(filename):
    with open(filename, 'r') as input_file:
        data = input_file.read().strip()

        return data

def solve_a(polymer):
    while True:
        changes_occured = False
        for index, char in enumerate(polymer):
            try:
                if (char.isupper() and polymer[index + 1] == char.lower()) or (char.islower() and polymer[index + 1] == char.upper()):
                    changes_occured = True
                    polymer = polymer[:index] + polymer[index+2:]
                    break
            except IndexError:
                break
        if not changes_occured:
            break

    return len(polymer)


def solve_b(data):
    s = data.lower()
    units = []
    for char in s:
        if char not in units:
            units.append(char)
    shortest = None
    units = ''.join(units)
    for unit in units:
        polymer = data
        polymer = polymer.replace(unit, '').replace(unit.upper(), '')
        while True:
            changes_occured = False
            for index, char in enumerate(polymer):
                try:
                    if (char.isupper() and polymer[index + 1] == char.lower()) or (char.islower() and polymer[index + 1] == char.upper()):
                        changes_occured = True
                        polymer = polymer[:index] + polymer[index+2:]
                        break
                except IndexError:
                    break
            if not changes_occured:
                shortest = len(polymer) if shortest is None else len(polymer) if len(polymer) < shortest else shortest
                break
    
    return shortest

if __name__ == '__main__':
    test_data = 'dabAcCaCBAcCcaDA'

    assert solve_a(test_data) == 10
    assert solve_b(test_data) == 4

    #data = load_input('challenges/day_05/input.txt')

    #answer_a = solve_a(data)
    #answer_b = solve_b(data)

    #print(f'Part A answer: {answer_a}   Part B answer: {answer_b}')
