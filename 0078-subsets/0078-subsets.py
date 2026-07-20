class Solution:
    def subset(self, ind, sub, ans, nums, n):
        if ind == n:
            ans.append(sub[:])         
            return
        
        self.subset(ind+1, sub, ans, nums, n)
        sub.append(nums[ind])

        self.subset(ind+1, sub, ans, nums, n)
        sub.pop()
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []
        
        self.subset(0, sub, ans, nums, len(nums))
        return ans