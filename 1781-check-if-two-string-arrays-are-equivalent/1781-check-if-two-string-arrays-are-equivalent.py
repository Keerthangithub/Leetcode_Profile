class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k=""
        d=""
        for i in word1:
            k+=i
        for i in word2:
            d+=i
        if k==d:
            return True
        return False