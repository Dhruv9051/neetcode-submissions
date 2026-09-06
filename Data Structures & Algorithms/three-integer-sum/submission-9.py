class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = [nums[i], nums[j], nums[k]]

        #                 triplet.sort()
        #                 if triplet not in  res:
        #                     res.append(triplet)

        # return res

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res