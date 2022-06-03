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

# DP 1+
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i], dp[i - 1] + nums[i]))
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

# DP 3
class Solution:
    def rob(self, nums):
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        return dp2
