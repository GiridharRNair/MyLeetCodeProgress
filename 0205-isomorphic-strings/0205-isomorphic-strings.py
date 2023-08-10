class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letter_dict = {}
        if len(s) != len(t):
            return False
        for idx in range(len(s)):
            if s[idx] in letter_dict:
                if letter_dict[s[idx]] != t[idx]:
                    return False
            else:
                # Check if the value t[idx] is already mapped to another key
                if t[idx] in letter_dict.values():
                    return False
                letter_dict[s[idx]] = t[idx]
        return True
