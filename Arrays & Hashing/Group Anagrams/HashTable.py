class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)
        for i in strs:
            character = [0] * 26
            for j in i:
                character[ord(j) - ord("a")] += 1
            d[tuple(character)].append(i)
        return list(d.values())
