class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping char count to list of anagrams
        for s in strs:
            count = [0] * 26 # for 26 chars

            for c in s:
                count[ord(c) - ord('a')] += 1 # ascii value of character - ascii value of a resulting to indexing. eg: a - a = 0, z - a = 25

            res[tuple(count)].append(s)
        
        return list(res.values())

# https://gemini.google.com/share/ec52aa8689b6