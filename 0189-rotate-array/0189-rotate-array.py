class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        while k >= n:
            k = k - n
        temp = []
        for i in range(n-k, n):
            temp.append(nums[i])

        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        
        for i in range(0, k):
            nums[i] = temp[i]
        
    