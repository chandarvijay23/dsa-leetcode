class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N^2)
        # Space Complexity (Best): O(N)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)

        # Create an array of lists (buckets) where the index represents frequency - 1.
        # `store[i]` will contain numbers that appeared `i+1` times.
        # The maximum possible frequency is `len(nums)`, so the array size is `len(nums)`.
        store = [[] for _ in range(len(nums))]

        # Dictionary to store the frequency of each number.
        d = {}

        # List to store the top k frequent numbers.
        returnlist = []

        # First pass: Count the frequency of each number.
        # This loop iterates N times. Dictionary operations (get, set) are O(1) on average.
        # In the worst case (hash collisions), dict operations can be O(N), leading to O(N^2) total.
        # Space complexity for `d` is O(U), where U is the number of unique elements (U <= N).
        for value in nums:
            d[value] = 1 + d.get(value, 0)

        # Second pass: Populate the 'store' array (effectively a bucket sort by frequency).
        # This loop iterates through the unique numbers and their counts, O(U) times.
        # Appending to a list is amortized O(1).
        # Space complexity for `store` is O(N) for the list of lists itself, plus O(U) for the stored elements.
        for value, count in d.items():
            # Frequencies are 1-indexed, list indices are 0-indexed.
            store[count - 1].append(value)

        # Third pass: Iterate from the highest possible frequency down to 1.
        # Collect elements until 'k' frequent numbers are found.
        # In the worst case for this step, we might iterate through all unique elements (O(U)).
        # The outer loop runs N times, but the inner loop accumulates elements.
        # The total number of elements processed across all `store[i]` lists is `U`.
        # Space complexity for `returnlist` is O(k).
        for i in range(len(store) - 1, -1, -1):
            for j in store[i]:
                returnlist.append(j)
                # If we have collected k elements, we can return the list.
                if len(returnlist) == k:
                    return returnlist
