class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> hash;

        for (auto it: nums1) {
            hash[it]++;
        }
        vector<int> result;
        for (auto it: nums2) {
            if (hash[it] > 0) {
                result.push_back(it);
                hash[it]--;
            }
        }

        return result;

    }
};