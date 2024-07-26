class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        c=0
        k=[]
        for i in range(len(mat)):
            c=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    c+=1
            k.append(c)
        return [k.index(max(k)),max(k)]