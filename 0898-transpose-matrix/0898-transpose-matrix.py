class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        k=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        #return k
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k[j][i]=matrix[i][j]
        return k

