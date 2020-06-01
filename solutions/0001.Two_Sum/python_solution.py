class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = {}
        for i, num in enumerate(nums):
            if num not in sums:
                sums[target - num] = i
            else:
                return [sums[num], i]