class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                position = ord(c) - ord('a')
                key[position] += 1

            groups.setdefault(tuple(key), []).append(s)

        return [x for x in groups.values()]