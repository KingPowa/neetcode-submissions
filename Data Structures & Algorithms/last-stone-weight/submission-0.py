class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_max = [-s for s in stones]
        heapq.heapify(stones_max)
        while len(stones_max) > 0:
            largest_1 = -heapq.heappop(stones_max)
            if len(stones_max) > 0:
                largest_2 = -heapq.heappop(stones_max)
                if largest_1 > largest_2:
                    heapq.heappush(stones_max, largest_2 - largest_1)
            else:
                return largest_1
        return 0