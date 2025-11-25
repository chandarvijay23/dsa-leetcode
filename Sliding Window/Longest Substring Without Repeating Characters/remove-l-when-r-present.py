class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = l = 0
        hashset = set()
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            count = max(count, r - l + 1)
        return count