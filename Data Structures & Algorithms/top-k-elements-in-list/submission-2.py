class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in nums:
            count[i] = count.get(i, 0) + 1

        sorted_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

        return list(sorted_count.keys())[:k]