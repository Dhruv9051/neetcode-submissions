class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        
        for i in range(len(temperatures)):
            ptr = i + 1
            while ptr < len(temperatures):
                if temperatures[i] < temperatures[ptr]:
                    res.append(ptr-i)
                    break
                ptr += 1
            else:
                res.append(0)
        
        return res