class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        center = len(nums) // 2
        while (right >= left):
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
                center = left + (right - left) // 2
            else:
                right = center - 1            
                center = (right - left) // 2
        return -1
            

        