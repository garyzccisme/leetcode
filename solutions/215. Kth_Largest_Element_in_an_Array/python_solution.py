# Directly use build in sorted()
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

# Heap Sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# Quick Sort
# To be optimized
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sort = self.quick_sort(nums)
        return sort[-k]

    def quick_sort(self, target):
        if len(target) <= 1:
            return target
        pivot = target.pop(0)
        left, right = [], []
        for num in target:
            if num <= pivot:
                left.append(num)
            else:
                right.append(num)
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

