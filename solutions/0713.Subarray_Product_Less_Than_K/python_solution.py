class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1: return 0
        window = 1
        left, ans = 0, 0
        for right in range(len(nums)):
            window *= nums[right]
            while window >= k:
                window /= nums[left]
                left += 1
            ans += right - left + 1
        return ans