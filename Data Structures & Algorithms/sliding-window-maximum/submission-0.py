from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        results = []

        left = 0
        for right in range(len(nums)):
            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(right)
            if right - left + 1 >= k:
                while queue and queue[0] < left:
                    queue.popleft()

                if queue:
                    results.append(nums[queue[0]])
                
                left += 1

        return results
