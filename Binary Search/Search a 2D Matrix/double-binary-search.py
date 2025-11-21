class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        top, bottom = 0, rows - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bottom = middle -1
            else:
                break
        
        if not top  <= bottom:
            return False

        left, right = 0, cols - 1

        while left <= right:
            m = (left + right) // 2
            if target > matrix[middle][m]:
                left = m + 1
            elif target < matrix[middle][m]:
                right = m- 1
            else:
                return True
        return False     