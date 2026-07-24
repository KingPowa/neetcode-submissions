class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 2: return []
        # Order nums
        nums.sort()
        triplets = set()
        for index in range(len(nums)):
            target = -nums[index]
            start = index + 1
            end = len(nums)-1
            while start < end and start != end:
                if nums[start] + nums[end] == target:
                    triplets.add((nums[index], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
        return list([list(x) for x in triplets])


