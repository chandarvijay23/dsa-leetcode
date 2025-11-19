class Solution:

    def encode(self, strs: List[str]) -> str:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O((M + N*D)^2)
        # Time Complexity (Worst): O((M + N*D)^2)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(M + N*D)
        # Space Complexity (Worst): O(M + N*D)
        s = ''
        for i in strs:
            s += str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(L_encoded)
        # Time Complexity (Worst): O(L_encoded)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(M + N)
        # Space Complexity (Worst): O(M + N)
        length = ''
        l = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                l.append(s[i + 1 : i + 1 + int(length)])
                i = i + 1 + int(length)
                length = ''
            else:
                length += s[i]
                i += 1
        return l
