from collections import deque
from functools import lru_cache
from pathlib import Path


def parse_input() -> tuple[list[list[str]], tuple[int, int]]:
    matrix = []
    with Path("./input.txt").open() as f:
        matrix = [list(line.strip()) for line in f]

    start = (0, 0)
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == "S":
                start = (row, column)
                break
    return matrix, start

class Part1:
    def __init__(self):
        self.visited = set()
        self.splits = 0

    def count_splits(self, matrix, start):
        queue = deque([(start[0], start[1])])
        while queue:
            next_x, next_y = queue.popleft()

            if next_x+1 < len(matrix) and matrix[next_x+1][next_y] == ".":
                next_x = next_x+1
                if (next_x, next_y) not in self.visited:
                    self.visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
            elif next_x+1 < len(matrix) and matrix[next_x+1][next_y] == "^":
                left_y = next_y - 1
                right_y = next_y + 1
                if (next_x, left_y) not in self.visited and left_y >= 0 and next_x < len(matrix) and matrix[next_x][left_y] == ".":
                    self.visited.add((next_x, left_y))
                    queue.append((next_x, left_y))
                if (next_x, right_y) not in self.visited and right_y < len(matrix[0]) and next_x < len(matrix) and matrix[next_x][right_y] == ".":
                    self.visited.add((next_x, right_y))
                    queue.append((next_x, right_y))

                self.splits += 1

        return self.splits

class Part2:
    def __init__(self):
        self.paths = {}

    def dfs(self, matrix, x, y) -> int:
        original_x = x
        original_y = y
        if (x, y) in self.paths:
            return self.paths[(x, y)]

        while x < len(matrix) and (matrix[x][y] == "." or matrix[x][y] == "S"):
            x += 1

        if x == len(matrix):
            return 1

        left = 0
        right = 0
        if matrix[x][y] == "^":
            x += 1
            left_y = y - 1
            right_y = y + 1

            if left_y >= 0 and (x, left_y):
                left = self.dfs(matrix, x, left_y)
            if right_y < len(matrix[0]) and (x, right_y):
                right = self.dfs(matrix, x, right_y)
        self.paths[(original_x, original_y)] = left + right
        return left + right



matrix, start = parse_input()
print(Part1().count_splits(matrix, start))

print(Part2().dfs(matrix, start[0], start[1]))