class Solution {
public:
    bool check(vector<int>& nums) {
        int n = nums.size();

        vector<int> A = nums;
        sort(A.begin(), A.end());

        int i = 1;

        while (i < n && nums[i] >= nums[i - 1]) {
            i++;
        }

        if (i == n) {
            return true;
        }

        int x = n - i;

        for (int j = 0; j < n; j++) {
            if (nums[j] != A[(j + x) % n]) {
                return false;
            }
        }

        return true;
    }
};