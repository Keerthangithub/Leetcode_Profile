class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        k=[]
        s=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in k:
                k.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1 and nums2[i] not in s:
                s.append(nums2[i])
        return [k,s]

