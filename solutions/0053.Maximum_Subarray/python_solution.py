class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum, sub_sum = nums[0], nums[0]
        for num in nums[1:]:
            if sub_sum >= 0:
                sub_sum += num
            else:
                sub_sum = num
            max_sum = max(max_sum, sub_sum)
        return max_sum