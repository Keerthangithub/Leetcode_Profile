class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        h=[]
        k=list(set(nums1))
        x=list(set(nums2))
        y=list(set(nums3))
        z=k+x+y
        d={}
        for i in z:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>=2:
                h.append(i)
        return h