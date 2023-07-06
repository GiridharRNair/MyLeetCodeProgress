class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # set with all the areas
#         areas = set()
        
#         # iterate thru heights
#         for i in range(len(height)):
#             for j in range(i, len(height)):
#                 areas.add(min(height[i], height[j]) * (j - i))
        
#         return max(areas)

        left = 0
        right = len(height) - 1
        area = 0
        while left <= right:
            area = max(min(height[left], height[right]) * (right - left), area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return area
            