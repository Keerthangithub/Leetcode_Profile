class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d=""
        for i in digits:
            d+=str(i)
        z=str(int(d)+1)
        k=[]
        for i in z:
            k.append(int(i))
        return k