class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]]=names[i]
        names=[]
        heights.sort(reverse=True)
        for i in heights:
            for j,k in d.items():
                if i==j:
                    names.append(k)
        return names