class Solution:
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