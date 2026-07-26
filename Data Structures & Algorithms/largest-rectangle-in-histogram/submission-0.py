class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestArea = -float("infinity")

        for curr_index in range(len(heights)):
            height = heights[curr_index]
            moving_left, moving_right = curr_index - 1, curr_index + 1
            width = 1
            while moving_right < len(heights) and heights[moving_right] >= height:
                width += 1
                moving_right += 1
            while moving_left >= 0 and heights[moving_left] >= height:
                width += 1
                moving_left -= 1
            if width * height > largestArea:
                largestArea = width * height
        return largestArea
            