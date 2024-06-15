class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        k=[]
        for i in range(len(nums1)):
            k.append(nums2[i]-nums1[i])
        return k[0]