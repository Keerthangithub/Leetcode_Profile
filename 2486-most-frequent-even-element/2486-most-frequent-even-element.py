class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        s=0
        f=[]
        for i in nums:
            if i not in d and i%2==0:
                d[i]=1
            if i in d and i%2==0:
                d[i]+=1
        #return d
        for i,j in d.items():
            if s<j:
                s=j
        for i,j in d.items():
            if j==s:
                f.append(i)
        if f==[]:
            return -1
        return min(f)
        '''v=[]
        f=[]
        for i in nums:
            if i%2==0:
                v.append(i)
        v.sort()
        for i in v:
            f.append(v.count(i))'''
        
        '''for i in v:
            if i in d:
                d[i]+=1
            elif i not in d:
                d[i]=1
        for i,j in d.items():
            c=j
            break
        for i,j in d.items():
            if c>=j:
                return i
        return -1'''

        
        