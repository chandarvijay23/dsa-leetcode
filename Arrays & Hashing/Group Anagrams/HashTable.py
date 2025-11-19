from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity (Best): O(N * K)
        # Time Complexity (Average): O(N * K)
        # Time Complexity (Worst): O(N * K)
        # Space Complexity (Best): O(N * K)
        # Space Complexity (Average): O(N * K)
        # Space Complexity (Worst): O(N * K)
        # N is the number of strings in 'strs'.
        # K is the maximum length of a string in 'strs'.
        # C is the size of the alphabet (26 for lowercase English letters).
        # Time complexity for each string: O(K) to build frequency array + O(C) to create tuple + O(1) for dictionary operation (average).
        # This simplifies to O(K) per string. Total N strings: O(N * K).
        # Space complexity: The dictionary stores N strings, each up to K length, plus N keys (tuples of size C).
        # This results in O(N*K) for string data and O(N*C) for keys. Total O(N*K) as C is constant.

        # Initialize a dictionary where keys will be frequency tuples and values will be lists of anagrams.
        d = defaultdict(list)

        # Iterate through each string in the input list.
        for s in strs:
            # Initialize a frequency array for 26 lowercase English letters.
            # Each index corresponds to a letter (e.g., 0 for 'a', 1 for 'b', etc.).
            character_counts = [0] * 26

            # Iterate through each character in the current string.
            for char in s:
                # Increment the count for the corresponding character.
                # ord(char) - ord('a') gives the 0-based index for the character.
                character_counts[ord(char) - ord('a')] += 1

            # Convert the frequency array to a tuple. Tuples are hashable and can be used as dictionary keys.
            # This tuple uniquely represents the anagram group for the current string.
            # Append the current string to the list associated with its frequency tuple key.
            d[tuple(character_counts)].append(s)

        # Return a list of all the values from the dictionary.
        # Each value is a list of strings that are anagrams of each other.
        return list(d.values())
