class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        k={}
        v=[]
        n=list(set(nums1))
        d=list(set(nums2))
        x=n+d
        for i in x:
            if i in k:
                k[i]+=1
            else:
                k[i]=1
        for i,j in k.items():
            if j>=2:
                v.append(i)
        if v==[]:
            return -1
        return min(v)