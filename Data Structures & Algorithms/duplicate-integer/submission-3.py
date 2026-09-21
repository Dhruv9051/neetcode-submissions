class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1 = {}

        for n in nums:
            map1[n] = 1 + map1.get(n, 0)
        
        for v in map1.values():
            if v > 1:
                return True
        
        return False