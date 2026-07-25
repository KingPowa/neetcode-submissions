class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums
        curr_maximum, num_of_maximums = -float("infinity"), 0
        
        # for first windows, calculate
        for i in range(0, k):
            if nums[i] == curr_maximum:
                num_of_maximums += 1
            elif curr_maximum < nums[i]:
                curr_maximum = max(curr_maximum, nums[i])
                num_of_maximums = 1
            
        maximums = [curr_maximum]
        for r in range(k, len(nums)):
            num = nums[r]
            if num == curr_maximum:
                num_of_maximums += 1
            elif curr_maximum < num:
                curr_maximum = max(curr_maximum, num)
                num_of_maximums = 1

            # look at the number being removed and update if maximum
            if nums[r-k] == curr_maximum:
                num_of_maximums -= 1
            
            # To decide what to append, we look at the current maximum
            if num_of_maximums >= 1:
                maximums.append(curr_maximum)
            else:
                # Compute new maximum again.
                curr_maximum, num_of_maximums = -float("infinity"), 0
                for explore in range(r-k+1, r+1):
                    if nums[explore] == curr_maximum:
                        num_of_maximums += 1
                    elif curr_maximum < nums[explore]:
                        curr_maximum = max(curr_maximum, nums[explore])
                        num_of_maximums = 1
                maximums.append(curr_maximum)
        return maximums
                
