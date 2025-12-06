from pathlib import Path


def parse_input():
    all_ranges = []
    with Path("./input.txt").open() as f:
        line = f.readline()
        for range_id in line.split(","):
            first_last = range_id.split("-")
            all_ranges.append((int(first_last[0]), int(first_last[1])))
    return all_ranges


class Part1:
    def is_invalid(self, current_id: str) -> bool:
        str_len = len(current_id)
        if str_len % 2 != 0:
            return False
        return current_id[: str_len // 2] == current_id[str_len // 2 :]

    def solution(self, input_data: list) -> int:
        res = 0
        for start, end in input_data:
            for id_ in range(start, end + 1):
                res += id_ if self.is_invalid(str(id_)) else 0
        return res


class Part2:
    def is_invalid(self, current_id: str) -> bool:
        str_len = len(current_id)
        for i in range(1, (str_len // 2) + 1):
            if str_len % i == 0:
                current_values = []
                counter = 0
                while True:
                    current_values.append(current_id[i * counter : i * counter + i])
                    counter += 1
                    if i * counter + i > str_len:
                        break
                if len(set(current_values)) == 1:
                    return True
            counter += 1
        return False

    def solution(self, input_data: list) -> int:
        res = 0
        for start, end in input_data:
            for id_ in range(start, end + 1):
                res += id_ if self.is_invalid(str(id_)) else 0
        return res


ranges = parse_input()
part_1 = Part1().solution(ranges)
print(part_1)
part_2 = Part2().solution(ranges)
print(part_2)
