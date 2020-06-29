# Greedy DFS with Stack
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Store all tickets into dict and sort
        self.path = collections.defaultdict(list)
        for depart, arrive in tickets:
            heapq.heappush(self.path[depart], arrive)

        return self.dfs('JFK', ['JFK'], [])

    def dfs(self, depart, pre_path, cross):
        """
        Greedy Travel!

        For each depart, start travelling with lexical order.
        For each cross point, add the point index into stack.
        After main path finished, backtrack each cross point and insert previously missing cycle branch path into main path.

        Args:
            depart: String, departure airport
            pre_path: List, visited path
            cross: List, stack to store crossings

        Returns: List, travel path

        """
        while self.path[depart]:

            # Meet crossing, add index into cross
            if len(self.path[depart]) > 1:
                cross.append(len(pre_path) - 1)

            # Travel with the lexcial smallest airport
            depart = heapq.heappop(self.path[depart])
            pre_path.append(depart)

        # Check if there's any crossing
        while cross:
            cross_idx = cross.pop()
            cross_depart = pre_path[cross_idx]

            # Insert the circle path into the crossing point
            pre_path[cross_idx:cross_idx + 1] = self.dfs(cross_depart, [cross_depart], [])
        return pre_path

# Eulerian Path
class Solution(object):
    def findItinerary(self, tickets):

        self.flightMap = collections.defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
        # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort(reverse=True)

        self.result = []
        print(self.flightMap)
        self.DFS('JFK')

        # reconstruct the route backwards
        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)