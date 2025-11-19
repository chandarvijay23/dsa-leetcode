class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity (Best): O(1)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(1)
        # Space Complexity (Average): O(1)
        # Space Complexity (Worst): O(1)
        l, r = 0, len(numbers) - 1

        while l < r:
            the_sum = numbers[l] + numbers[r]
            if the_sum < target:
                l += 1
            elif the_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
