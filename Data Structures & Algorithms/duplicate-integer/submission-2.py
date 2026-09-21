class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        
        for v in map.values():
            if v > 1:
                return True
        
        return False