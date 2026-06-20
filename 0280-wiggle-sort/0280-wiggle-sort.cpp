class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<int> ret;

        int i = 0;
        int j = nums.size() - 1;

        while(i <= j) {
            ret.push_back(nums[i]);
            if(i != j) {
                ret.push_back(nums[j]);
            }
            i++; j--;
        }

        nums = ret;
    }
};