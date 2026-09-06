class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getFreq(string):
            freq = {}
            for i in range(len(string)):
                freq[string[i]] = 1 + freq.get(string[i], 0)
            return freq

        freq1 = {}
        windowSize = len(s1)
        for i in range(windowSize):
            freq1[s1[i]] = 1 + freq1.get(s1[i], 0)

        for j in range(len(s2)):
            l, r = j, j + windowSize - 1
            
            if getFreq(s2[l : r + 1]) == freq1:
                return True
        
        return False

