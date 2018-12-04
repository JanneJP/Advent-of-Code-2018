from __future__ import annotations
from typing import List

class Rectangle():
    def __init__(self, name: str, measurements: tuple, coordinates: tuple):
        self.name = name
        self.width, self.height = measurements
        self.min_x, self.min_y = [coord + 1 for coord in coordinates]
        self.max_x = self.min_x + self.width - 1
        self.max_y = self.min_y + self.height - 1
    
    def overlaps(self, other: Rectangle) -> bool:
        return (((self.min_x <= other.max_x) and (self.max_x >= other.min_x)) and ((self.min_y <= other.max_y) and (self.max_y >= other.min_y)))

def load_input(filename: str) -> List[Rectangle]:
    rectangles = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            tmp = line.strip().split(' ')

            rectangle = Rectangle(tmp[0].replace('#', ''), tuple([int(x) for x in tmp[3].split('x')]), tuple([int(x) for x in tmp[2].replace(':', '').split(',')]))

            rectangles.append(rectangle)

    return rectangles

def solve_a(rectangles: List[Rectangle]) -> int:
    width = max([rectangle.max_x for rectangle in rectangles])
    height = max([rectangle.max_y for rectangle in rectangles])
    
    grid = [[0 for x in range(width)] for row in range(height)]

    for rectangle in rectangles:
        for y in range(rectangle.min_y-1, rectangle.max_y):
            for x in range(rectangle.min_x-1, rectangle.max_x):
                grid[y][x] += 1

    return sum([sum([1 if grid[y][x] > 1 else 0 for x in range(width)]) for y in range(height)])

def solve_b(rectangles: List[Rectangle]) -> str:
    for rect_1 in rectangles:
        overlaps = False
        for rect_2 in rectangles:
            if rect_1.name == rect_2.name:
                continue
            
            if rect_1.overlaps(rect_2):
                overlaps = True
                break
        
        if not overlaps:
            return rect_1.name

if __name__ == '__main__':
    rectangles = load_input('challenges/day_03/input.txt')

    test = [Rectangle('1', (4, 4), (1, 3)),Rectangle('2', (4, 4), (3, 1)),Rectangle('3', (2, 2), (5, 5))]

    assert solve_a(test) == 4
    assert solve_b(test) == '3'

    answer_a = solve_a(rectangles)
    answer_b = solve_b(rectangles)

    print(f'Part A answer: {answer_a}   Part B answer: {answer_b}')
