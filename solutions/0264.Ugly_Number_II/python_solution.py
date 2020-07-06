class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_list = [1]

        # (ugly number, factor, index)
        ugly_heap = [(2, 2, 0), (3, 3, 0), (5, 5, 0)]

        while n > 1:
            next_ugly, factor, idx = heapq.heappop(ugly_heap)
            # Prevent duplicates
            if next_ugly != ugly_list[-1]:
                ugly_list.append(next_ugly)
                n -= 1
            idx += 1
            heapq.heappush(ugly_heap, (factor * ugly_list[idx], factor, idx))

        return ugly_list[-1]
