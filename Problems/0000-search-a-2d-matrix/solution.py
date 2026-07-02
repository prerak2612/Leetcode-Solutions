class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        s = 0
        e = (r*c) - 1
        while(s <= e):
            mid = (s+e) // 2
            row = mid // c
            col = mid % c
            if matrix[row][col] == target:
                return True
            elif target >  matrix[row][col]:
                s = mid + 1
            else:
                e = mid - 1
        return False
