from pathlib import Path


def parse_input() -> list[list[int]]:
    with Path("./toy_input.txt").open() as f:
        return [[int(item) for item in line.strip()] for line in f]


class Part1:
    @staticmethod
    def solution(batteries: list[list[int]]) -> int:
        output_joltage = 0
        for bank in batteries:
            max_right: dict[int, int] = {}
            current_max = 0
            for index in range(len(bank) - 2, -1, -1):
                if index + 1 in max_right:
                    max_right[index] = max(max_right[index + 1], bank[index + 1])
                else:
                    max_right[index] = bank[index + 1]
            for index in range(len(bank) - 1):
                current_value = int(str(bank[index]) + str(max_right[index]))
                current_max = max(current_max, current_value)
            output_joltage += current_max

        return output_joltage


batteries = parse_input()
print(Part1.solution(batteries))
