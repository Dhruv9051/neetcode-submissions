class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

            if count[i] > 1:
                return True
        
        return False