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
