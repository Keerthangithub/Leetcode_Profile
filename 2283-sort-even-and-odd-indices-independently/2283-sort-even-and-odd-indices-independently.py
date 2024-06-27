class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        k=[]
        s=[]
        u,o=0,0
        for i in range(len(nums)):
            if i%2!=0:
                k.append(nums[i])
            else:
                s.append(nums[i])
        k.sort(reverse=True)
        s.sort()
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=s[u]
                u+=1
            else:
                nums[i]=k[o]
                o+=1
        return nums
        