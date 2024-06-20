class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        k=[]
        c=0
        for i in words:
            for j in i:
                if j==x:
                    k.append(c)
                    break
            c+=1
        if k==[]:
            return []
        return k