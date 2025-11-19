class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity (Best): O(N)
        # Time Complexity (Average): O(N)
        # Time Complexity (Worst): O(N)
        # Space Complexity (Best): O(N)
        # Space Complexity (Average): O(N)
        # Space Complexity (Worst): O(N)
        product = [1] * len(nums)

        prefix = 1
        suffix = 1

        # First pass: calculate prefix products and store them
        # product[i] will hold the product of all elements to its left
        for i in range(len(nums)):
            product[i] *= prefix
            prefix *= nums[i]

        # Second pass: calculate suffix products and combine with prefix products
        # product[i] (which has left product) is multiplied by right product
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]
        
        return product
