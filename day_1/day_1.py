from pathlib import Path


def parse_input():
    with Path("./input.txt").open() as f:
        return [(line[0], int(line[1:])) for line in f]


class Part1:
    @staticmethod
    def solution(input_data: list) -> int:
        current_position = 50
        result = 0
        max_value = 100

        for direction, distance in input_data:
            distance = distance if direction == "R" else -distance
            current_position = (current_position + distance) % max_value
            result += 1 if current_position == 0 else 0

        return result


class Part2:
    @staticmethod
    def solution(input_data: list) -> int:
        current_position = 50
        result = 0
        max_value = 100

        for direction, distance in input_data:
            distance = distance if direction == "R" else -distance
            difference = current_position + distance
            if difference < 0:
                if current_position != 0:
                    result += 1
                result += abs(difference) // max_value
            elif difference in (0, max_value):
                result += 1
            elif difference > max_value:
                result += 1
                result += abs(distance - (max_value - current_position)) // max_value

            current_position = (current_position + distance) % max_value

        return result


input_data = parse_input()
part_1_result = Part1.solution(input_data)
print("Part 1: ", part_1_result)

part_2_result = Part2.solution(input_data)
print("Part 2: ", part_2_result)
print("Part 2: ", part_2_result)
