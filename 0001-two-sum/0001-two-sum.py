class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = dict()
        for index, num in enumerate(nums):
            if (target - num) in dict_nums:
                return [index, dict_nums[target - num]]
            else:
                dict_nums[num] = index
        return None
        
        