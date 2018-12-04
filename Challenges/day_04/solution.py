import datetime

def load_input(filename):
    with open(filename, 'r') as input_file:
        return [line.strip() for line in input_file]

def parse_data(raw_data):
    return sorted([{'timestamp': ' '.join([line.split(' ')[0], line.split(' ')[1]]), 'event':' '.join(line.split(' ')[2:])} for line in [line.replace('[', '').replace(']', '') for line in raw_data]], key=lambda x: datetime.datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M'))

def solve_a(log):
    guards = {}
    active_guard = None
    start = None
    end = None

    for entry in log:
        if entry['event'] == 'falls asleep':
            start = int(entry['timestamp'].split(' ')[1].split(':')[1])
        elif entry['event'] == 'wakes up':
            end = int(entry['timestamp'].split(' ')[1].split(':')[1])
            if active_guard not in guards:
                guards[active_guard] = {'name': active_guard, 'minutes': [0 for _ in range(60)], 'total': 0}
            guards[active_guard]['total'] += (end - start)
            for i in range(start, end):
                guards[active_guard]['minutes'][i] += 1
        elif entry['event'][:5] == 'Guard':
            active_guard = str(entry['event'].split(' ')[1].replace('#', ''))
    
    highest_total_minutes = 0
    top_guard_name = None
    for guard in guards:
        if guards[guard]['total'] > highest_total_minutes:
            top_guard_name = guards[guard]['name']
            highest_total_minutes = guards[guard]['total']

    return guards[top_guard_name]['minutes'].index(max(guards[top_guard_name]['minutes'])) * int(guards[top_guard_name]['name'])

def solve_b(log):
    guards = {}
    active_guard = None
    start = None
    end = None
    for entry in log:
        if entry['event'] == 'falls asleep':
            start = int(entry['timestamp'].split(' ')[1].split(':')[1])
        elif entry['event'] == 'wakes up':
            end = int(entry['timestamp'].split(' ')[1].split(':')[1])
            dif = end - start
            if active_guard not in guards:
                guards[active_guard] = {'name': active_guard, 'minutes': [0 for _ in range(60)], 'total': 0}
            guards[active_guard]['total'] += dif
            for i in range(start, end):
                guards[active_guard]['minutes'][i] += 1
        elif entry['event'][:5] == 'Guard':
            num = str(entry['event'].split(' ')[1].replace('#', ''))
            active_guard = num
        else:
            print(f'Unknown event: {entry}')
    
    a = 0
    b = 0
    c = 0

    for guard_name in guards:
        guard = guards[guard_name]
        for i in range(len(guard['minutes'])):
            if guard['minutes'][i] > a:
                a = guard['minutes'][i]
                b = guard['name']
                c = i

    return int(b) * int(c)

if __name__ == '__main__':
    test = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up'
    ]

    test_data = parse_data(test)

    assert solve_a(test_data) == 240
    assert solve_b(test_data) == 4455

    raw_data = load_input('challenges/day_04/input.txt')

    data = parse_data(raw_data)

    answer_a = solve_a(data)
    answer_b = solve_b(data)

    assert answer_a == 102688
    assert answer_b == 56901

    print(f'Part A answer: {answer_a}   Part B answer: {answer_b}')
