class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max_key = max(d, key=d.get)
        k=0
        for i,j in d.items():
            if i==max_key:
                c+=j
                k=j
            if j==k:
                c+=j

        return c-k