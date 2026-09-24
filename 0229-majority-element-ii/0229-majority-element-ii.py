class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ele1 = float('-inf')
        ele2 = float('-inf')
        cnt1 = 0
        cnt2 = 0

        for i in range(n):
            if cnt1 == 0 and ele2 != nums[i]:
                cnt1 = 1
                ele1 = nums[i]
            elif cnt2 == 0 and ele1 != nums[i]:
                cnt2 = 1 
                ele2 = nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == ele1:
                cnt1 += 1
            if num == ele2:
                cnt2 += 1
        
        mini = n // 3 + 1
        result = []

        if cnt1 >= mini:
            result.append(ele1)
        if cnt2 >= mini and ele2 != ele1:
            result.append(ele2)
        
        return result