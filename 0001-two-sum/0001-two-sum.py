class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = dict()
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in pairs:
                return [nums.index(diff), idx]
            pairs[num] = diff
            
            
            
            """
            [3, 3]
            [2, 4]
            
            """
        