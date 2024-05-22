class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = dict()
        for idx, num in enumerate(nums):
            if target - num in complement:
                return [idx, complement[target - num]]
            complement[num] = idx