class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            d=""
            d=str(i)
            d=max(d)*len(str(i))
            s+=int(d)
        return s

                