class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count_s1 = {}
        total_got = 0
        for s in s1:
            if s not in count_s1:
                count_s1[s] = 0
            count_s1[s] += 1
            total_got += 1
        
        start, end, current_count = 0, 0, {}
        while end < len(s2):
            while end < len(s2) and s2[end] in count_s1:
                if total_got == len(s1): 
                    start = end 
                if s2[end] not in current_count:
                    current_count[s2[end]] = 0
                if current_count[s2[end]] < count_s1[s2[end]]:
                    # We got one
                    current_count[s2[end]] +=  1
                    total_got -= 1
                    if total_got == 0:
                        return True
                    end += 1
                elif current_count[s2[end]] == count_s1[s2[end]]:
                    # We got one, but it was already found
                    current_count[s2[start]] -= 1
                    start += 1
                    total_got += 1
            # Reset
            total_got = len(s1)
            current_count = {}
            end += 1
        return False



             