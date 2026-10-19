class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        highest_left_wall = 0
        highest_right_wall = 0
        while left < right:
            if height[left] < height[right]:
                highest_left_wall = max(highest_left_wall, height[left])
                water += highest_left_wall - height[left]
                left += 1
            else:
                highest_right_wall = max(highest_right_wall, height[right])
                water += highest_right_wall - height[right]
                right -= 1
                
        return water