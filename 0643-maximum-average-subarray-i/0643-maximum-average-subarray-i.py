class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:        
        max_sum = sum(nums[:k])
        temp_sum = max_sum
        idx = 0
        right = k
        while (right < len(nums)):
            temp_sum -= nums[idx]
            temp_sum += nums[right]
            max_sum = max(max_sum, temp_sum)
            idx += 1
            right += 1
        return max_sum / k
                
                