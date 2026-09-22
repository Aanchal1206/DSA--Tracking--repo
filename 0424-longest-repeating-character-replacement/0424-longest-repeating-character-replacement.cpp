class Solution {
public:
    int characterReplacement(string s, int k) {
        
        vector<int> count(26, 0);

        int left = 0;
        int maxFrequency = 0;
        int answer = 0;

        for (int right = 0; right < s.length(); right++) {

            count[s[right] - 'A']++;

            maxFrequency = max(maxFrequency,
                               count[s[right] - 'A']);

            while ((right - left + 1) - maxFrequency > k) {
                count[s[left] - 'A']--;
                left++;
            }

            answer = max(answer, right - left + 1);
        }

        return answer;
    }
};