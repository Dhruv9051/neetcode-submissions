class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # final = []
        # for i in range(len(nums)):
        #     collate = []
        #     res = 1
        #     l, r = i-1, i+1
        #     while l >= 0:
        #         collate.append(nums[l])
        #         l-=1
        #     while r < len(nums):
        #         collate.append(nums[r])
        #         r+=1
        #     for j in collate:
        #         res *= j
        #     final.append(res)
        # return final

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        