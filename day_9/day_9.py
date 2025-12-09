from collections import deque
from pathlib import Path


def parse_input() -> list[list]:
    with Path("./toy_input.txt").open() as f:
        return [[int(item) for item in line.strip().split(",")] for line in f]


class Part1:
    def largest_area(self, red_tiles) -> int:
        max_area = 0
        for index in range(len(red_tiles)):
            x_1, y_1 = red_tiles[index]
            for j in range(index + 1):
                x_2, y_2 = red_tiles[j]
                current_area = ((max(x_1, x_2) - min(x_1, x_2)) + 1) * ((max(y_1, y_2) - min(y_1, y_2)) + 1)
                max_area = max(max_area, current_area)

        return max_area


red_tiles = parse_input()
print(Part1().largest_area(red_tiles))
