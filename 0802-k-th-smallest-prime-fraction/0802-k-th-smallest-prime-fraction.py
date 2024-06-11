class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        s=[]
        d=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                s.append(arr[i]/arr[j])
        s.sort()
        d=s[k-1]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if d==arr[i]/arr[j]:
                    return [arr[i],arr[j]]
        