class Solution:
    def mask(self, c):
        return 1 << ord(c)

    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        maximum = 0
        seen = 0
        while end < len(s):
            masked = self.mask(s[end])
            while seen & masked != 0:
                seen ^= self.mask(s[start])
                start += 1
            seen |= masked
            end += 1
            maximum = max(maximum, end - start)
        return maximum
