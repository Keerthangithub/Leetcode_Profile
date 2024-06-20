class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        d=""
        for i in words:
            d+=i[0]
        if d==s:
            return True
        return False