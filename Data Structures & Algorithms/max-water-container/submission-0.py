class Solution:
    def calcArea(self, a, b, l):
        return min(a,b) * l

    def maxArea(self, heights: List[int]) -> int:
        maximum_area = 0
        a, b = 0, len(heights) - 1
        while b > a and b != a:
            if self.calcArea(heights[a], heights[b], b - a) > maximum_area:
                maximum_area = self.calcArea(heights[a], heights[b], b - a)
            if heights[a] >= heights[b]:
                b -= 1
            else:
                a += 1
        return maximum_area
            