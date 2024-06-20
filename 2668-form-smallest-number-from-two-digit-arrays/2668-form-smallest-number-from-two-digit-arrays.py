class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            for j in nums2:
                if i==j:
                    return i
        d=""
        d+=str(min(nums1))
        d+=str(min(nums2))
        if int(d)>int(d[::-1]):
            return int(d[::-1])
        return int(d)
