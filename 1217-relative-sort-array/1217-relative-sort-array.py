class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k=[]
        v=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    k.append(i)
        for i in arr1:
            if i not in k:
                v.append(i)
        v.sort()
        k.extend(v)
        return k
    