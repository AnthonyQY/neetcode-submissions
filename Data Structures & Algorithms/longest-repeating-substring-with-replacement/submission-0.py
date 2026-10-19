class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        longest = 0

        left = 0
        for c in s:
            count[c] = count.get(c, 0) + 1
            while sum(count.values()) - max(count.values()) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            longest = max(longest, sum(count.values()))

        return longest