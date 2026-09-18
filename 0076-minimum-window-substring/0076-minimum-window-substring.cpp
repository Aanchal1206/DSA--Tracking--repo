class Solution {
public:
    string minWindow(string s, string t) {
        
        if (t.length() > s.length()) {
            return "";
        }

        unordered_map<char, int> need;
        unordered_map<char, int> window;

        for (char c : t) {
            need[c]++;
        }

        int left = 0;
        int have = 0;
        int required = t.length();

        int start = 0;
        int minLength = INT_MAX;

        for (int right = 0; right < s.length(); right++) {
            
            char c = s[right];
            window[c]++;

            if (need.find(c) != need.end() && window[c] <= need[c]) {
                have++;
            }

            while (have == required) {
                
                if (right - left + 1 < minLength) {
                    minLength = right - left + 1;
                    start = left;
                }

                char leftChar = s[left];
                window[leftChar]--;

                if (need.find(leftChar) != need.end() &&
                    window[leftChar] < need[leftChar]) {
                    have--;
                }

                left++;
            }
        }

        if (minLength == INT_MAX) {
            return "";
        }

        return s.substr(start, minLength);
    }
};
