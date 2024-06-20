class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        k=[]
        for i in sentences:
            c=1
            for j in i:
                if j==" ":
                    c+=1
            k.append(c)
        return max(k)