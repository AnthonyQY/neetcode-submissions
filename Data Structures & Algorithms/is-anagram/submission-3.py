class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_table = {}
        for c in s:
            freq_table[c] = freq_table.get(c, 0) + 1

        for c in t:
            freq_table[c] = freq_table.get(c, 0) - 1
            if freq_table[c] == 0:
                del freq_table[c]
            elif freq_table[c] == -1:
                return False

        return len(freq_table) == 0