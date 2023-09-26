class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            num = nums[idx] 
            nums[idx] = num * num
        return sorted(nums)