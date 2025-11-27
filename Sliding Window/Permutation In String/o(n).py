class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(len(s1)):
            l1[ord(s1[i]) - ord('a')] += 1
            l2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if l1[i] == l2[i] else 0)
            
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            newindex = ord(s2[i]) - ord('a')
            oldindex = ord(s2[i - len(s1)]) - ord('a')
            
            if l2[newindex] == l1[newindex]: #check if the index already contributes to matches - if yes decrement
                matches -= 1
            l2[newindex] += 1
            if l2[newindex] == l1[newindex]:
                matches += 1

            if l2[oldindex] == l1[oldindex]:
                matches -= 1
            l2[oldindex] -= 1
            if l2[oldindex] == l1[oldindex]:
                matches += 1
        
        return (matches == 26)