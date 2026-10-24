class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = []
        largest_area = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                current_index = stack.pop()
                rect_height = heights[current_index]
                left_index = stack[-1] if stack else -1
            
                right_index = i
                right_height = height
                rect_width = right_index - left_index - 1

                area = rect_width * rect_height
                largest_area = max(area, largest_area)

            stack.append(i)
        return largest_area