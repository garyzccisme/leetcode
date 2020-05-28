class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        while len(ans) <= num:
            new = [i + 1 for i in ans]
            ans += new
        return ans[:num + 1]