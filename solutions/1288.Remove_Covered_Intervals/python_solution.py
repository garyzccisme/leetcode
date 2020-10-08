class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans, pre_right = len(intervals), -1
        for _, right in intervals:
            if right <= pre_right:
                ans -= 1
            else:
                pre_right = right
        return ans