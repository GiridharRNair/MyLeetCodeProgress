class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_flowerbed = [0] + flowerbed + [0]
        count = 0
        for idx in range(1, len(new_flowerbed) - 1):
            if new_flowerbed[idx - 1] == 0 and new_flowerbed[idx + 1] == 0 and new_flowerbed[idx] == 0:
                new_flowerbed[idx] = 1
                count += 1
        return count >= n
        