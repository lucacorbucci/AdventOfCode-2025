from pathlib import Path


def parse_input() -> tuple[list[tuple[int, int]], list[int]]:
    lines = []
    with Path("./input.txt").open() as f:
        lines = [line.strip() for line in f]
    ranges, available_ids = [], []
    for line in lines:
        split_line = line.split("-")
        if len(split_line) == 2:
            ranges.append((int(split_line[0]), int(split_line[1])))
        elif line == "":
            continue
        else:
            available_ids.append(int(line))
    return ranges, available_ids


class Part1:
    def merge_overlapping_ranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        res = []
        left = 0
        right = 1
        current_range = ranges[left]

        while right < len(ranges):
            max_range = max(current_range[0], ranges[right][0])
            min_range = min(current_range[1], ranges[right][1])

            if max_range < min_range:
                current_range = (min(current_range[0], ranges[right][0]), max(current_range[1], ranges[right][1]))
                right += 1
            else:
                res.append(current_range)
                left = right
                right += 1
                current_range = ranges[left]
        if current_range not in res:
            res.append(current_range)
        return res

    def solution(self, ranges: list[tuple[int, int]], available_ids: list[int]) -> int:
        count = 0
        ranges = sorted(ranges, key=lambda x: x[0])

        ranges = self.merge_overlapping_ranges(ranges)

        for id_ in available_ids:
            for start, end in ranges:
                if start <= id_ <= end:
                    count += 1
                    break
        return count


class Part2:
    def merge_overlapping_ranges(self, ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        res = []
        left = 0
        right = 1
        current_range = ranges[left]

        while right < len(ranges):
            max_range = max(current_range[0], ranges[right][0])
            min_range = min(current_range[1], ranges[right][1])

            if max_range <= min_range:
                current_range = (min(current_range[0], ranges[right][0]), max(current_range[1], ranges[right][1]))
                right += 1
            else:
                res.append(current_range)
                left = right
                right += 1
                current_range = ranges[left]
        if current_range not in res:
            res.append(current_range)
        return res

    def solution(self, ranges: list[tuple[int, int]]) -> int:
        count = 0
        ranges = sorted(ranges, key=lambda x: x[0])

        ranges = self.merge_overlapping_ranges(ranges)
        for start, end in ranges:
            count += end - start + 1

        return count


ranges, available_ids = parse_input()
print(Part1().solution(ranges, available_ids))
print(Part2().solution(ranges))
