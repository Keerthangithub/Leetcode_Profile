class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k=[]
        d,c=0,0
        for i in range(len(candies)):
            d=candies[i]+extraCandies
            c=0
            for j in range(len(candies)):
                if d>=candies[j]:
                    c+=1
            if c==len(candies):
                k.append(True)
            else:
                k.append(False)
        return k