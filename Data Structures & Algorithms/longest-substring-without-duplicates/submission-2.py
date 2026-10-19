class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        left = 0
        for right in range(len(s)):
            character = s[right]
            
            while right < len(s) and character in window:
                window.remove(s[left])
                left += 1

            window.add(character)
            
            longest = max(longest, len(window))
        return longest