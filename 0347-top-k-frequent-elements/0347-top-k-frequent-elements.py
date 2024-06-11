class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        s,v=[],[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            s.append(d[i])
        s.sort(reverse=True)
        for i in range(k):
            f=max(s)
            for i,j in d.items():
                if f==j:
                    v.append(i)
                    s.remove(f)
                    d.pop(i)
                    break
        return v
