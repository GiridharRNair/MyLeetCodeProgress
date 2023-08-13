class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        prefix = 1
        for idx, num in enumerate(nums):
            out[idx] = prefix
            prefix *= num
        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            out[idx] *= postfix
            postfix *= nums[idx]
        return out
        
