class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[0]*len(nums)
        a,b=0,len(nums)-1
        for i in nums:
            if i%2==0:
                k[a]=i
                a+=1
            else:
                k[b]=i
                b-=1
        return k