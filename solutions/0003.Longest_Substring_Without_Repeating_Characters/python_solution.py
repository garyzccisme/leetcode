class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_sub = 0
        sub = ''
        for letter in s:
            idx = sub.find(letter)
            if idx == -1:
                sub += letter
            else:
                sub = sub[idx + 1:] + letter
            max_sub = max(max_sub, len(sub))

        return max_sub


# Better Solution using Hash Table
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        start = 0
        idx_dict = {}
        for i, letter in enumerate(s):
            idx = idx_dict.get(letter, -1) + 1
            if idx > start:
                start = idx
            max_sub = max(max_sub, i - start + 1)
            idx_dict[letter] = i
        return max_sub