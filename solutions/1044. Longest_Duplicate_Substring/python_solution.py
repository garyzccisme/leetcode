class Solution:
    def longestDupSubstring(self, S: str) -> str:

        if len(S) == len(set(S)):
            return ''

        # Convert S into 26 hex format
        self.nums = [ord(S[i]) - ord('a') for i in range(len(S))]

        # Set up modulus to avoid overflow
        self.modulus = 2 ** 32

        # Binary Search
        left = 0
        right = len(S)

        while left < right - 1:
            mid = (left + right) // 2

            if self.search(mid) == -1:
                right = mid
            else:
                left = mid

        start = self.search(left)
        return S[start:start + left]

    def search(self, window):

        # Calculate initial value
        value = 0
        for i in range(window):
            value = (value * 26 + self.nums[i]) % self.modulus

        # Store seen value into hash set
        seen = {value}

        # Precalculate constant 26 ** window % modulus
        cons = pow(26, window, self.modulus)

        for start in range(1, len(self.nums) - window + 1):
            # Calculate rolling hash in O(1) time
            value = (value * 26 - self.nums[start - 1] * cons + self.nums[start + window - 1]) % self.modulus
            if value in seen:
                return start
            else:
                seen.add(value)
        return -1