class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        k=[]
        s=[]
        for i in range(len(grid)):
            for j in range(len(grid)):
                k.append(grid[i][j])
        d={}
        for i in k:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>1:
                s.append(i)
        f=len(grid)
        for i in range(1,(f**2)+1):
            if i not in k:
                s.append(i)
        return s