class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums == []:
            return -1

        head = 0
        tail = len(nums) - 1
        if nums[head] == target:
            return head
        if nums[tail] == target:
            return tail

        while head < tail - 1:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[head]:
                if nums[head] < target < nums[mid]:
                    tail = mid
                else:
                    head = mid
            elif nums[mid] < nums[tail]:
                if nums[mid] < target < nums[tail]:
                    head = mid
                else:
                    tail = mid

        return -1