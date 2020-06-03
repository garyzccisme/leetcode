# Hash Map
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        # Use Hash Map to avoid duplicated calculation
        ans = []
        ans_set = set()
        seen_num1 = set()

        for i, num1 in enumerate(nums[:-2]):
            if num1 not in seen_num1:
                seen_num1.add(num1)

                two_sum_dict = {}
                for num2 in nums[i + 1:]:
                    if num2 in two_sum_dict:
                        found = tuple(sorted([num1, num2, two_sum_dict[num2]]))

                        if found not in ans_set:
                            ans_set.add(found)
                            ans.append(found)
                    else:
                        two_sum_dict[- num1 - num2] = num2
        return ans

# Two Pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()
        output = set()

        for i, num in enumerate(nums[:-2]):

            # Skip duplicates
            if i > 0 and num == nums[i - 1]:
                continue

            head = i + 1
            tail = len(nums) - 1
            while head < tail:
                if nums[head] + nums[tail] < -num:
                    head += 1
                elif nums[head] + nums[tail] > -num:
                    tail -= 1
                else:
                    output.add((num, nums[head], nums[tail]))
                    head += 1
                    tail -= 1

        return list(output)

