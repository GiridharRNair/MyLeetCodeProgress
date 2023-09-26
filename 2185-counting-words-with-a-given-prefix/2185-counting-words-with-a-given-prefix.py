class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if pref in word and word.index(pref) == 0:
                count += 1
        return count