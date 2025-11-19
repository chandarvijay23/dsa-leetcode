class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)

        d1 = {}
        d2 = {}

        # Anagrams must have the same length.
        # This check provides an O(1) best-case time complexity if lengths differ.
        if len(s) != len(t):
            return False

        # Populate the frequency map for string 's'.
        # This loop iterates N times, where N is the length of string s.
        # Dictionary operations (insertion, lookup, update) take O(1) time on average.
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        
        # Populate the frequency map for string 't'.
        # This loop also iterates N times, as len(s) == len(t) has been confirmed.
        # Dictionary operations take O(1) time on average.
        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        
        # Compare the two frequency maps.
        # Dictionary comparison takes time proportional to the number of distinct characters.
        # If the alphabet size is considered constant (e.g., 26 for English letters, 256 for ASCII),
        # this operation takes O(1) time. In the worst case, it's O(N) if all characters are distinct
        # and the alphabet is not bounded to a small constant. Given typical anagram problem contexts,
        # alphabet size is usually treated as a constant.
        return d1 == d2
