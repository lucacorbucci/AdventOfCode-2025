from functools import lru_cache
from pathlib import Path


def parse_input() -> dict:
    graph = {}

    with Path("./input.txt").open() as f:
        for line in f:
            line = line.strip()
            split_line = line.split(":")
            source = split_line[0]
            destinations = split_line[1].split(" ")
            graph[source] = destinations[1:]

    return graph

class Part1:


    def dfs(self, node: str, graph: dict, dest: str)-> int:
        if node == dest:
            return 1

        count = 0
        if node in graph:
            for neigh in graph[node]:
                count += self.dfs(neigh, graph, dest)

        return count

    def solution(self, graph, source, dest):
        return self.dfs(source, graph, dest)


class Part2:
    
    def __init__(self, graph, dest):
        self.graph = graph
        self.dest = dest

    @lru_cache(maxsize=None)
    def dfs(self, node: str, found_dac, found_fft)-> int :
        if node == "fft":
            found_fft = True
        if node == "dac":
            found_dac = True

        if found_dac and found_fft and node == self.dest:
            return 1

        count = 0
        if node in graph:
            for neigh in graph[node]:
                count += self.dfs(neigh, found_dac, found_fft)
        return count


    def solution(self, source):
        return self.dfs(source, False, False)


graph = parse_input()
source = "you"
dest = "out"
print(Part1().solution(graph, source, dest))

source = "svr"
dest = "out"
print(Part2(graph=graph, dest=dest).solution(source))