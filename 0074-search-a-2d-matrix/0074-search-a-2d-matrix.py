class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        if top > bottom:
            return False
        row = (top + bottom) // 2
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True
        return False
