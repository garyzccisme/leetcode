# Start from highest
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for person, num in people:
            if num >= len(ans):
                ans.append([person, num])
            else:
                ans.insert(num, [person, num])
        return ans

# Start from shortest
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        # Sort by height ascending, counts descending
        people.sort(key=lambda x: (x[0], -x[1]))
        # Initialize the final list with 0
        ans = [0] * len(people)

        for height, num in people:
            # zero_count stores the number of 0s (which is the # of greater numbers) when iterating
            # idx means the index in final list
            zero_count, idx = 0, 0
            # When the # of 0s reachs the required number, then stop the iteration
            # idx would be the final index
            while zero_count <= num:
                if ans[idx] == 0:
                    zero_count += 1
                idx += 1

            ans[idx - 1] = [height, num]
        return ans