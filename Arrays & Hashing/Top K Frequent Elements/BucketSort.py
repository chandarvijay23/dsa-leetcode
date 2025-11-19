class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = [[] for _ in range(len(nums))]
        d = {}
        returnlist = []
        for value in nums:
            d[value] = 1 + d.get(value, 0)
        for value, count in d.items():
            store[count - 1].append(value)
        for i in range(len(store) - 1, -1, -1):
            for j in store[i]:
                returnlist.append(j)
                if len(returnlist) == k:
                    return returnlist
