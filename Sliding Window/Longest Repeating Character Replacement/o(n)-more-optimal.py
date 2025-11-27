class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        output = 0
        hashmap = {}
        maxf = 0
        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            maxf = hashmap[s[r]] if hashmap[s[r]] > maxf else maxf
            if (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1  
            output = max(output, r - l + 1)
        return output