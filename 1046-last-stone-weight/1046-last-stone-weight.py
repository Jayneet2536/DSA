class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        stone = [-s for s in stones]
        heapq.heapify(stone)

        while(len(stone) > 1):
            first = heapq.heappop(stone)
            second = heapq.heappop(stone)

            heapq.heappush(stone, first - second)
        
        stone.append(0)
        return abs(stone[0])