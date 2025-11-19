class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity (Best): O(n)
        # Time Complexity (Average): O(n)
        # Time Complexity (Worst): O(n)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        if len(s) != len(t):
            return False

        # Initialize a frequency array for lowercase English letters.
        # The size is fixed at 26, independent of input string length.
        counts = [0] * 26

        # Iterate through both strings simultaneously.
        # For each character in 's', increment its count.
        # For each character in 't', decrement its count.
        # This effectively compares frequencies in a single pass.
        for i in range(len(s)):
            # Convert character to an index (0-25)
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        # If 's' and 't' are anagrams, all counts in the frequency array
        # must be zero, meaning each character appeared an equal number of times.
        # This check iterates over a fixed-size array (26 elements).
        return all(c == 0 for c in counts)
