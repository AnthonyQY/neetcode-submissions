class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_count = {}
        for c in s1:
            target_count[c] = target_count.get(c, 0) + 1

        window_count = {}
        left = 0
        for right, c in enumerate(s2):
            window_count[c] = window_count.get(c, 0) + 1
            if (right - left + 1) > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            if (right - left + 1) == len(s1):
                if window_count == target_count:
                    return True

        return False