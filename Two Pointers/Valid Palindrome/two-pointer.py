class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

    def alphanum(self, c: str) -> bool:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(1)
        # Time Complexity (Worst): O(1)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        return (ord("a") <= ord(c) <= ord("z") or
                ord("A") <= ord(c) <= ord("Z") or
                ord("0") <= ord(c) <= ord("9"))
