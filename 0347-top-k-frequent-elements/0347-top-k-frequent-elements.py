class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pairs = {num: 0 for num in nums}
        for num in nums:
            pairs[num] += 1
        out = []
        values = sorted(pairs.values(), reverse=True)
        k_highest = values[:k]
        for key in pairs:
            if pairs[key] in k_highest:
                out.append(key)
        return out