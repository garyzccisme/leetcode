class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # The container dp that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        dp = {-1: set()}
        nums.sort()
        for num in nums:
            dp[num] = max([dp[k] for k in dp if num % k == 0], key=len).union({num})
        return list(max(dp.values(), key=len))
