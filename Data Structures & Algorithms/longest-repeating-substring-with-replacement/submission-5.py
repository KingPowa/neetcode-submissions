from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        char_count, most_frequent = defaultdict(int),0
        longest = 1
        for end in range(len(s)):
            char_count[s[end]] += 1
            if char_count[s[end]] > most_frequent:
                most_frequent = char_count[s[end]]
            while (end - start + 1) - most_frequent > k:
                char_count[s[start]] -= 1
                start += 1
            longest = max(end-start+1, longest)
        return longest

            
            

