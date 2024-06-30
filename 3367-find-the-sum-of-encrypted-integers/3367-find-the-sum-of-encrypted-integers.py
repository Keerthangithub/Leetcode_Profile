class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        k=[]
        s=0
        d=""
        for i in nums:
            k.append(str(i))
        for i in k:
            d=max(i)*len(i)
            s+=int(d)
        return s

                