class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = dict()
        for i in range(len(nums)):
            if (nums[i] in hashMap) and (abs(i - hashMap[nums[i]]) <= k):
                return True
            else:
                hashMap[nums[i]] = i
        return False
                
        
        # for i in range(len(nums)):
        #     numCheck = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False