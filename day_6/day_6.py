from functools import reduce
from operator import mul
from pathlib import Path


def parse_input() -> tuple[list[list[int]], list[str]]:
    lines = []
    with Path("./input.txt").open() as f:
        lines = [line.strip().split() for line in f]

    matrix = []
    ops = []
    for i in range(len(lines[0])):
        tmp = [int(lines[j][i]) for j in range(len(lines) - 1)]
        matrix.append(tmp)
    ops = lines[-1]

    return matrix, ops


def parse_input_part_2() -> tuple[list[list[int]], list[str]]:
    with Path("./input.txt").open() as f:
        lines = list(f)
    matrix = []
    ops: list[str] = []
    group: list[int] = []
    for i in range(len(lines[0])):
        column = [lines[j][i] for j in range(len(lines) - 1) if lines[j][i].isdigit()]
        if column == []:
            matrix.append(group)
            group = []
        else:
            group.append(int("".join(column)))
    ops = lines[-1].strip().split()

    return matrix, ops


class Part1:
    @staticmethod
    def solution(matrix: list[list[int]], ops: list[str]) -> int:
        res = 0
        for numbers, op in zip(matrix, ops):
            if op == "*":
                res += reduce(mul, numbers, 1)
            else:
                res += sum(numbers)
        return res


matrix, ops = parse_input()
print(Part1.solution(matrix, ops))
matrix, ops = parse_input_part_2()
print(Part1.solution(matrix, ops))
