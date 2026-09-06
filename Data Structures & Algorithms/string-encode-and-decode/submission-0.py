class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i : j])

            # The string starts 1 char after the '#'
            string_start = j + 1
            string_end = string_start + length
            res.append(s[string_start : string_end])
            
            # Move the main pointer 'i' to the start of the next chunk
            i = string_end
            
        return res