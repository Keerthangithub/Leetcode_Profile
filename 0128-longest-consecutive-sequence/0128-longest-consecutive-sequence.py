class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        c=1
        s=list(set(nums))
        s.sort()
        k=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]-1:
                c+=1
            else:
                k.append(c)
                c=1
        k.append(c)
        return max(k)