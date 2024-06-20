class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        k=[]
        j=n
        for i in range(n):
            k.append(nums[i])
            while j<len(nums):
                k.append(nums[j])
                j+=1
                break
        return k