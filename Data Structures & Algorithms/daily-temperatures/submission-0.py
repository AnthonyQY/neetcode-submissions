class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_decreasing = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while monotonic_decreasing and temperatures[monotonic_decreasing[-1]] < t:
                day = monotonic_decreasing.pop()
                result[day] = i - day
            monotonic_decreasing.append(i)
            
        return result