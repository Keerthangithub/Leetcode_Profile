class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j=0
        while j<len(matrix):
            m=0
            n=len(matrix[j])-1
            while m<=n:
                k=(m+n)//2
                if matrix[j][k]==target:
                    return True
                elif target>matrix[j][k]:
                    m=k+1
                else:
                    n=k-1 
            j+=1
        return False