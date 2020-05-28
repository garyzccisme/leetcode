class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        # Store relationships in dict
        self.dislike_dict = collections.defaultdict(list)
        for a, b in dislikes:
            self.dislike_dict[a].append(b)
            self.dislike_dict[b].append(a)

        # 0 = unvisited, 1 = group 1, -1 = group -1
        self.status = [0] * N
        for n in range(1, N):
            if not self.status[n - 1]:
                if not self.dfs(n, 1):
                    return False
        return True

    def dfs(self, n, group):

        # if there's a cycle and the group conflicts status
        if self.status[n - 1]:
            if group != self.status[n - 1]:
                return False
            else:
                return True

        # divide unvisited point in to group
        self.status[n - 1] = group
        for dislike in self.dislike_dict[n]:
            # early stop
            if not self.dfs(dislike, -group): return False
        return True

