# Python built-in function
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]

# Quick Sort, Divide & Conquer
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        sort(0, len(points) - 1, K)
        return points[:K]

# Max Heap
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # maxHeap of size k, one pass through list
        # if heap size < k or heap.peek > currDist, pop and push

        heap = []
        for i in range(len(points)):
            x, y = points[i]
            dist = x ** 2 + y ** 2
            if len(heap) < K:
                heapq.heappush(heap, (-dist, i))
            elif heap[0][0] < -dist:
                heapq.heappushpop(heap, (-dist, i))

        ans = []
        for j in range(len(heap)):
            dist, index = heap[j]
            ans.append(points[index])

        return ans
