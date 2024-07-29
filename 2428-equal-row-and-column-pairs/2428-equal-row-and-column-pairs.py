class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c,f,k=0,0,0
        while f<len(grid):
            for i in range(len(grid)):
                s=[]
                for j in range(len(grid[0])):
                    s.append(grid[j][i])
                if grid[k]==s:
                    c+=1
            f+=1
            k+=1
        return c