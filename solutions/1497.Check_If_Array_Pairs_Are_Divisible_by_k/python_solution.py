# Solution 1: Two Sum
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        mod_dict = collections.defaultdict(int)
        pairs = 0

        for num in arr:
            mod = num % k
            if mod_dict[mod] > 0:
                pairs += 1
                mod_dict[mod] -= 1
            else:
                mod_dict[(k - mod) % k] += 1

        return pairs == len(arr) // 2


# Solution 2: Count List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        mod_list = [0] * k

        for num in arr:
            mod_list[num % k] += 1

        for i in range(1, k // 2 + 1):
            if mod_list[i] != mod_list[k - i]:
                return False
            if i == k - i and mod_list[i] % 2:
                return False
        return True
