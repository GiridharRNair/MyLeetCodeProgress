class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            #loop
            for idx in range(len(digits) - 1, -1, -1):
                if digits[idx] == 9:
                    digits[idx] = 0
                else:
                    digits[idx] += 1
                    return digits
            return [1] + digits
                    
        else:
            num = digits[-1]
            num += 1
            digits[-1] = num
            return digits