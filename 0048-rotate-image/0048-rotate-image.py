class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                r[j][i]=matrix[i][j]
        for i in r:
            i.reverse()
        for i in range(len(r)):
            matrix[i]=r[i]
        