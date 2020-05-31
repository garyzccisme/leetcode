# BFS
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        road = collections.defaultdict(set)
        # 1, -1 means the road direction
        for a, b in connections:
            road[a].add((b, 1))
            road[b].add((a, -1))

        count = 0
        visit = [0] * n
        travel = collections.deque([0])

        while travel:
            city = travel.popleft()
            visit[city] = 1
            for next_city, direction in road[city]:
                if not visit[next_city]:
                    travel.append(next_city)
                    if direction == 1:
                        count += 1
        return count

# DFS
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        self.road = collections.defaultdict(set)
        # 1, -1 means the road direction
        for a, b in connections:
            self.road[a].add((b, 1))
            self.road[b].add((a, -1))

        self.count = 0
        self.visit = [0] * n
        self.dfs(0)
        return self.count

    def dfs(self, city):
        self.visit[city] = 1
        for next_city, direction in self.road[city]:
            if not self.visit[next_city]:
                if direction == 1:
                    self.count += 1
                self.dfs(next_city)