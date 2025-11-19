class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if value + nums[l] + nums[r] < 0:
                        l += 1
                    elif value + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        result.append([value, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
        return result
