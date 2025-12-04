from pathlib import Path


def parse_input() -> list[list[str]]:
    with Path("./input.txt").open() as f:
        return [list(line.strip()) for line in f]


class Part1:
    def solution(self, grid):
        rolls = self.find_rolls(grid)
        count_rolls = 0
        for roll_x, roll_y in rolls:
            count_rolls += 1 if self.is_valid(roll_x, roll_y) else 0
        return count_rolls

    def is_valid(self, pos_x, pos_y) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1, -1), (-1, 1), (1, -1)]
        count = 0
        max_rolls = 4
        for dir_x, dir_y in directions:
            new_x = pos_x+dir_x
            new_y = pos_y + dir_y
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                count += 1 if grid[new_x][new_y] == "@" else 0
        return count < max_rolls



    def find_rolls(self, grid: list[list[str]])-> list[tuple[int, int]]:
        rolls: list[tuple[int, int]] = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "@":
                    rolls.append((x, y))
        return rolls

class Part2:
    def solution(self, grid):

        count_rolls = 0
        while True:
            current_counter = 0
            rolls = self.find_rolls(grid)
            for roll_x, roll_y in rolls:
                if self.is_valid(roll_x, roll_y):
                    current_counter += 1
                    grid[roll_x][roll_y] = "."
            if current_counter == 0:
                break
            count_rolls += current_counter
        return count_rolls

    def is_valid(self, pos_x, pos_y) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1,1), (-1, -1), (-1, 1), (1, -1)]
        count = 0
        max_rolls = 4
        for dir_x, dir_y in directions:
            new_x = pos_x+dir_x
            new_y = pos_y + dir_y
            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]):
                count += 1 if grid[new_x][new_y] == "@" else 0
        return count < max_rolls



    def find_rolls(self, grid: list[list[str]])-> list[tuple[int, int]]:
        rolls: list[tuple[int, int]] = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "@":
                    rolls.append((x, y))
        return rolls

grid = parse_input()
print(Part1().solution(grid))
print(Part2().solution(grid))


