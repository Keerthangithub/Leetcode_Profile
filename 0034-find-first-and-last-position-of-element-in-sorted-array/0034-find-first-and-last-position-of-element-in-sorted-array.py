class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=[]
        l=[]
        if len(nums)==0:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                s.append(i)
        if s==[]:
            return [-1,-1]
        if len(s)==1:
            s.append(s[0])
            return s
        if len(s)>=3:
            l.append(s[0])
            l.append(s[len(s)-1])
            return l
        return s
        '''for i in range(len(nums)):
            if len(nums)==1:
                if nums[i]==target:
                    return [i,i]
                else:
                    c=0
            if len(nums)==2:
                if nums[0]==nums[1] and nums[i]==target:
                    return [0,1]
                if nums[0]!=nums[1] and nums[i]==target:
                    return [i,i]
                else:
                    c=0
            if nums[i]==target:
                c=1
                s.append(i)
            if len(s)==2:
                break
            if nums[i]!=target:
                c=0
        if c==0:
            return [-1,-1]
        else:
            return s'''