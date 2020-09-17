# DP 1
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = nums[:2]
        for i in range(2, len(nums)):
            if i >= 3:
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1], nums[i] + dp[i - 3]))
            else:
                dp.append(max(nums[i] + dp[i - 2], dp[i - 1]))
        return dp[-1]

# DP 2
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0, nums[0], nums[1]]
        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2]) + nums[i])
        return max(dp[-2:])
