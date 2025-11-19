class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(N)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        hash_nums = set(nums)  # Convert the list to a hash set for O(1) average time lookups.
        longest = 0            # Initialize the variable to store the maximum consecutive sequence length found.

        # Iterate through each unique number present in the hash set.
        # This approach ensures each number is processed efficiently.
        for i in hash_nums:
            # Check if the current number 'i' is the potential start of a consecutive sequence.
            # If 'i - 1' is NOT in the hash set, it means 'i' is not preceded by 'i-1',
            # hence 'i' is a starting point of a new consecutive sequence.
            # This optimization prevents reprocessing numbers that are part of an already-found sequence.
            if (i - 1) not in hash_nums:
                length = 1  # Initialize the current sequence length to 1 (for the number 'i' itself).

                # Incrementally check for subsequent numbers in the sequence.
                # 'i + length' checks for the next expected number in the consecutive sequence.
                while (i + length) in hash_nums:
                    length += 1  # Extend the length of the current sequence.
                
                # After finding the full length of the current consecutive sequence,
                # update 'longest' if the current sequence is longer.
                longest = max(length, longest)
                
        return longest  # Return the overall longest consecutive sequence found.
