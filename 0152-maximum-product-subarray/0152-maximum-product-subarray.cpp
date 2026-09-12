class Solution {
public:
    int maxProduct(vector<int>& nums) {

        int maxProduct = nums[0];
        int minProduct = nums[0];
        int answer = nums[0];

        for (int i = 1; i < nums.size(); i++) {

            int current = nums[i];

            int newMax = max({current,
                              current * maxProduct,
                              current * minProduct});

            int newMin = min({current,
                              current * maxProduct,
                              current * minProduct});

            maxProduct = newMax;
            minProduct = newMin;

            answer = max(answer, maxProduct);
        }

        return answer;
    }
};