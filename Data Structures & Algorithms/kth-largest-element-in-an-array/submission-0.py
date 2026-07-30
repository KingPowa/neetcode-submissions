class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_nums = [-n for n in nums]
        heapq.heapify(max_nums)
        for _ in range(k-1):
            heapq.heappop(max_nums)
        return -heapq.heappop(max_nums)
        