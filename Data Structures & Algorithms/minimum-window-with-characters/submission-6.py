class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_chars = {}
        for c in t:
            target_chars[c] = target_chars.get(c, 0) + 1

        window_chars = {}
        shortest_left = 0
        shortest_right = -1
        shortest_length = float("inf")
        left = 0

        have = 0
        need = len(target_chars)
        for right, c in enumerate(s):
            if c in target_chars:
                window_chars[c] = window_chars.get(c, 0) + 1
                if window_chars[c] == target_chars[c]:
                    have += 1
            while have == need:
                if right - left + 1 < shortest_length:
                    shortest_left = left
                    shortest_right = right
                    shortest_length = right - left + 1
                if s[left] in target_chars:
                    window_chars[s[left]] = window_chars.get(s[left], 1) - 1
                    if window_chars[s[left]] < target_chars[s[left]]:
                        have -= 1
                    if window_chars[s[left]] == 0:
                        del window_chars[s[left]]
                left += 1
        return s[shortest_left:shortest_right + 1]

