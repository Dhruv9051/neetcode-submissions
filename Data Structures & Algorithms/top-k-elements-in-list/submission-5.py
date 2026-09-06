class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # res = []
        # for i in nums:
        #     count[i] = count.get(i, 0) + 1

        # sorted_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}

        # return list(sorted_count.keys())[:k]

        # bucket sort
        # keep a hashmap to get count of all items
        # have a frequency array which would be list of lists -> 
        # this will keep the elements under their frequency counts -> 
        # so indexes would be the frequency and the lists under those would be the numbers who have that frequency
        # next will be result array which would be appended with the numbers from last to first

        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
