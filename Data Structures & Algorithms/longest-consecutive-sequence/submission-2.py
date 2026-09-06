# trick - get the start point for all sequences
class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     num_set = set(nums) 
    #     longest_count = 0
        
    #     # 2. Iterate through the set
    #     for num in num_set:
    #         # Check if it's the start of a sequence
    #         if num - 1 not in num_set:
    #             current_num = num
    #             current_count = 1  # Start counting at 1, not 0
                
    #             # 3. Safely check for the next consecutive numbers
    #             while current_num + 1 in num_set:
    #                 current_num += 1
    #                 current_count += 1
                    
    #             # Update the maximum count found so far
    #             longest_count = max(longest_count, current_count)

    #     return longest_count
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_count = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_count = 1
                while current_num + 1 in nums_set:
                    current_count += 1
                    current_num += 1
                longest_count = max(longest_count, current_count)

        return longest_count