class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix == [] or matrix == [[]]:
            return False

        W, H = len(matrix[0]), len(matrix)

        if matrix[0][0] == target or matrix[H - 1][W - 1] == target:
            return True
        if matrix[0][0] > target or matrix[H - 1][W - 1] < target:
            return False

        head = 0
        tail = W * H - 1

        while head < tail - 1:
            mid = (head + tail) // 2
            mid_value = matrix[mid // W][mid % W]
            if mid_value > target:
                tail = mid
            elif mid_value < target:
                head = mid
            else:
                return True

        return False
