class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s
    def decode(self, s: str) -> List[str]:
        length = ''
        l = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                l.append(s[i+1:i+1+int(length)])
                i = i+1+int(length)
                length = ''
            else:
                length += s[i]
                i += 1
        return l