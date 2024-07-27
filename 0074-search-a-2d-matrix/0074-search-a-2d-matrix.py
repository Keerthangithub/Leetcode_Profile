class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''if len(matrix)==1:
            if matrix[0][0]==target:
                return True'''
        j,i=0,0
        while i<len(matrix):
            x=0
            y=len(matrix[j])-1
            while x<=y:
                m=(x+y)//2
                if target==matrix[j][m]:
                    return True
                elif target>matrix[j][m]:
                    x=m+1
                else:
                    y=m-1
            j+=1
            i+=1
        return False