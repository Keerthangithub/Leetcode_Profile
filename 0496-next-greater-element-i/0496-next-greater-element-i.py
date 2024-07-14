class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=[]
        for i in range(len(nums1)):
            d=nums2.index(nums1[i])
            for j in range(d+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    k.append(nums2[j])
                    break
            if len(k)==i:
                k.append(-1)
        return k