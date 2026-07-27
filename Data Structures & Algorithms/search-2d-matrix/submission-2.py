class Solution:
    def aMatrix(self, index, m, n, matrix):
        j = index % n
        i = (index - j) // n
        return matrix[i][j]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        length = m*n
        start, end = 0, length - 1
        while start <= end:
            pivot = start + (end - start) // 2
            if self.aMatrix(pivot, m, n, matrix) == target:
                return True
            elif self.aMatrix(pivot, m, n, matrix) < target:
                start = pivot + 1
            elif self.aMatrix(pivot, m, n, matrix) > target:
                end = pivot - 1
        return False