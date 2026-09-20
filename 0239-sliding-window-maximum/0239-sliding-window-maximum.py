class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        ans = []
        n = len(nums)
        for i in range(n):
            if q and q[0] <= i - k:
                q.popleft()

            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            q.append(i)

            if i >= k-1:
                ans.append(nums[q[0]])
        return ans