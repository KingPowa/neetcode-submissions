class Solution:

    def canKokoEat(self, piles, h, rate):
        required_time = 0
        for p in piles:
            required_time += math.ceil(p/rate)
        return h >= required_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h: raise ValueError()
        max_rate = max(piles)
        min_rate = 1
        j = 0
        while min_rate <= max_rate:
            pivot_rate = min_rate + (max_rate - min_rate) // 2
            succeed = self.canKokoEat(piles, h, pivot_rate)
            if not succeed:
                min_rate = pivot_rate + 1
            elif succeed:
                max_rate = pivot_rate - 1
        return min_rate