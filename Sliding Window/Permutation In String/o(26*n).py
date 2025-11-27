class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(len(s1)):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s1), len(s2)):
            if l1 == l2:
                return True
            newindex = ord(s2[i]) - ord('a')
            oldindex = ord(s2[i - len(s1)]) - ord('a')
            l2[newindex] += 1
            l2[oldindex] -= 1
        
        return (l1 == l2)