class Solution:
    def isPalindrome(self, s: str) -> bool:
        foward = ''
        for char in s:
            if char.isalpha() or char.isdigit():
                foward += char.lower()
        backward = ''
        for char in reversed(foward):
            backward += char
        return backward == foward