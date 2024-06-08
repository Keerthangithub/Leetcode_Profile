class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=""
        for i in digits:
            d+=str(i)
        k=[]
        for i in str(int(d)+1):
            k.append(int(i))
        return k