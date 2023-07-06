class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_nums = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in nums_set:
                    current_length += 1
                    current_num += 1
                
                max_nums = max(current_length, max_nums)
        return max_nums