class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        s=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                s.append(arr[i]/arr[j])
        s.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if s[k-1]==arr[i]/arr[j]:
                    return [arr[i],arr[j]]
        