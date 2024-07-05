class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        k=list(set(word1))+list(set(word2))
        c=0
        for i in k:
            if abs(word1.count(i)-word2.count(i))>3:
                c=1
                return False
        if c!=1:
            return True
            
