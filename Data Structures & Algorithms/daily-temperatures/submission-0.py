class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        still_no_warmer = [0]
        result = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            while len(still_no_warmer)>0 and temperatures[i]>temperatures[still_no_warmer[-1]]:
                result[still_no_warmer[-1]] = i - still_no_warmer[-1]
                still_no_warmer.pop()
            still_no_warmer.append(i)
        return result

