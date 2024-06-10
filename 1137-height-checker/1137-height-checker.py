class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k=[]
        c=0
        for i in heights:
            k.append(i)
        k.sort()
        for i in range(len(heights)):
            if heights[i]!=k[i]:
                c+=1
        return c
