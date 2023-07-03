class Solution:
    def isValid(self, s: str) -> bool:
        para = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for bracket in s:
            if bracket in para:
                stack.append(bracket)
            elif (len(stack) == 0 or bracket != para[stack.pop()]):
                return False
        return len(stack) == 0