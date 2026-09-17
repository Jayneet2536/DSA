class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int actual_sum = 0;
        for (int i = 0; i <= n; i++) {
            actual_sum += i;
        }   

        int sum = accumulate(nums.begin(), nums.end(), 0);

        return actual_sum - sum;
    }
};