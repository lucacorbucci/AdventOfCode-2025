import math
from functools import reduce
from operator import mul
from pathlib import Path


def parse_input() -> list[list]:
    with Path("./input.txt").open() as f:
        return [[int(item) for item in line.strip().split(",")] for line in f]


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False
        else:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
                self.rank[u] += self.rank[v]
                self.size[u] += self.size[v]
            else:
                self.parent[u] = v
                self.rank[v] += self.rank[u]
                self.size[v] += self.size[u]

        return True

    def top_k_component_sizes(self, k) -> list[int]:
        # we go to the root of the component and then we get its size
        # we need to do this to avoid measuring the size of each component
        return sorted([self.size[i] for i in range(len(self.parent)) if self.parent[i] == i], reverse=True)[:k]

    def get_number_of_connected_components(self, n) -> int:
        return len({self.find(i) for i in range(n)})


class Part1:
    def __init__(self):
        self.distances = []

    def compute_distances(self, positions, max_junctions):
        distances = []
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x_i, y_i, z_i = positions[i]
                x_j, y_j, z_j = positions[j]
                distance = math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2 + (z_i - z_j) ** 2)
                distances.append((distance, i, j))
        self.distances = sorted(distances)[:max_junctions]

    def solution(self, positions, max_junctions) -> int:
        self.compute_distances(positions, max_junctions)
        dsu = DSU(len(positions))
        for _, i, j in self.distances:
            dsu.union(i, j)

        return reduce(mul, dsu.top_k_component_sizes(k=3), 1)


class Part2:
    def __init__(self):
        self.distances = []

    def compute_distances(self, positions):
        distances = []
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x_i, y_i, z_i = positions[i]
                x_j, y_j, z_j = positions[j]
                distance = math.sqrt((x_i - x_j) ** 2 + (y_i - y_j) ** 2 + (z_i - z_j) ** 2)
                distances.append((distance, i, j))
        self.distances = sorted(distances)

    def solution(self, positions) -> int:
        self.compute_distances(positions)
        num_positions = len(positions)
        dsu = DSU(num_positions)
        for _, i, j in self.distances:
            dsu.union(i, j)
            if dsu.get_number_of_connected_components(num_positions) == 1:
                break

        return positions[i][0] * positions[j][0]


positions = parse_input()
max_junctions = 1000
print(Part1().solution(positions, max_junctions))
print(Part2().solution(positions))
