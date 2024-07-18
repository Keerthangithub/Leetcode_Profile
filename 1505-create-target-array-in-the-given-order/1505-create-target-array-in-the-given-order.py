class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        d=0
        '''for i in range(len(nums)):
            k.append(0)
        for i in range(len(index)):
            for j in range(d,len(index)):
                k[i]=nums[j]
                d+=1
                break'''
        for i in range(len(nums)):
            if nums[i]==index[i]:
                target.insert(index[i], nums[i])
            else:
                target.insert(index[i], nums[i])
        return target