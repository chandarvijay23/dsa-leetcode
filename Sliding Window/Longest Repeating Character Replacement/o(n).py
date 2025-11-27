class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        output = 0
        hashmap = {}
        maxf = 0
        for r in range(len(s)):
            if s[r] in hashmap:
                hashmap[s[r]] += 1
            else:
                hashmap[s[r]] = 1
            maxf = hashmap[s[r]] if hashmap[s[r]] > maxf else maxf
            if (r - l + 1) - maxf <= k:
                output = max(output, r - l + 1)
            else:
                if hashmap[s[l]] > 0:
                    hashmap[s[l]] -= 1
                l += 1  
        return output