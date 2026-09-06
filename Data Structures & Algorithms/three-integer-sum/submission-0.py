class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: #check if current value is more than index 0 and its value is same as index 0 (duplication chheck)
                continue # continue in such case (curr loop skip)

            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+= 1
        return res

        # https://gemini.google.com/share/7e5ebf3e5ccc