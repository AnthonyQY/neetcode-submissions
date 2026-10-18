class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        results = []
        size = ""

        left = 0
        while left < len(s):
            c = s[left]
            if c.isnumeric():
                size += c
                left += 1
            elif c == "#":
                results.append(s[left + 1:left + 1 + int(size)])
                left += 1 + int(size)
                size = ""

        return results