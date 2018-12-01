
with open('challenges/day_01/input.txt', 'r') as input_file:
    data = [int(row.strip()) for row in input_file]

print(f'Part A answer: {sum(data)}')

visited = [0]
frequency = 0
index = 0

while True:
    new_frequency = frequency + data[index % len(data)]

    if new_frequency in visited:
        print(f'Part B answer: {new_frequency}')
        break

    frequency = new_frequency

    visited.append(new_frequency)

    index += 1
