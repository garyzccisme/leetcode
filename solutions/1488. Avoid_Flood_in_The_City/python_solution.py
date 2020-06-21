class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        ans = []

        # full stores current full lakes
        full = set()
        # dry stores dry plan for full lakes, the first is the earliest upcomming rain
        dry = []
        # for each lake, stores rain deque for it
        lakes = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            lakes[lake].append(i)

        for lake in rains:
            if lake:
                # If lake is already full, then it will be a flood
                if lake in full:
                    return []
                else:
                    full.add(lake)
                    ans.append(-1)
                    lakes[lake].popleft()
                    # If there are more rains for this lake later, store the next rains idx into dry
                    # dry is Heap so that the first one is always the smallest idx (earlist rain)
                    if lakes[lake]:
                        heapq.heappush(dry, lakes[lake][0])
            else:
                if dry:
                    next_dry = rains[heapq.heappop(dry)]
                    ans.append(next_dry)
                    full.remove(next_dry)
                else:
                    ans.append(1)

        return ans