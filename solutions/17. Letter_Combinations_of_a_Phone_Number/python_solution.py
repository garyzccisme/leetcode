class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        ans = self.dfs(digits, [])
        return ans

    def dfs(self, digits, comb):
        if not digits:
            return comb
        if not comb:
            return self.dfs(digits[1:], self.phone[digits[0]])

        next_comb = []
        for letter in self.phone[digits[0]]:
            for precomb in comb:
                next_comb.append(precomb + letter)
        return self.dfs(digits[1:], next_comb)