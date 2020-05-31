class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        road = collections.defaultdict(set)
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