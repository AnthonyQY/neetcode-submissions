import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        freq_table = {}
        for n in nums:
            freq_table[n] = freq_table.get(n, 0) + 1

        for num, count in freq_table.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [x[1] for x in heap]
        