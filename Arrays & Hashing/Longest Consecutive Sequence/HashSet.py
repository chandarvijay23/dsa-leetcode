class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_nums = set(nums)
        longest = 0

        for i in hash_nums:
            if (i-1) not in hash_nums:
                length = 1
                while i+length in hash_nums:
                    length += 1
                longest = max(length, longest)
                
        return longest