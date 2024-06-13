class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        d=""
        for i in words:
            d+=i
            if d!=s:
                continue
            else:
                return True
        return False