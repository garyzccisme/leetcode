# My Solution
class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        letter_dict = {}
        for i, letter in enumerate(S):
            if letter not in letter_dict:
                letter_dict[letter] = [i, i]
            else:
                letter_dict[letter][-1] = i

        pos = list(letter_dict.values())
        index = 0
        while index < len(pos) - 1:
            if pos[index][1] > pos[index + 1][0]:
                pos[index][1] = max(pos[index][1], pos[index + 1][1])
                pos.pop(index + 1)
            else:
                index += 1

        return [tail - head + 1 for head, tail in pos]

# Leetcode Solution
class Solution(object):
    def partitionLabels(self, S):

        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans