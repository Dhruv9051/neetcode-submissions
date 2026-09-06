class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            collate = []
            res = 1
            l, r = i-1, i+1
            while l >= 0:
                collate.append(nums[l])
                l-=1
            while r < len(nums):
                collate.append(nums[r])
                r+=1
            for j in collate:
                res *= j
            final.append(res)
        return final