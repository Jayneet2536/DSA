class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0

        max_cnt = 0
        cnt = 0

        while(r < len(nums)):
            if nums[r] == 1:
                cnt = r - l + 1
                max_cnt = max(cnt, max_cnt)
                r += 1
            else:
                cnt = 0
                r += 1
                l = r
                
            
        return max_cnt    
