class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            # Calculate what number we need to reach target
            complement = target - num
        
            # Check if we've seen the complement before
            if complement in seen:
                # Found it! Return the stored index and current index
                return [seen[complement], i]
            
            # Haven't found complement yet, store current number and index
            seen[num] = i         
