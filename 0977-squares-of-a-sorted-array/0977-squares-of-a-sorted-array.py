class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        low = 0
        high = len(nums) - 1
        while (low <= high):
            if abs(nums[low]) > abs(nums[high]):
                out.append(nums[low] ** 2)
                low += 1
            else:
                out.append(nums[high] ** 2)
                high -= 1
        return reversed(out)
                