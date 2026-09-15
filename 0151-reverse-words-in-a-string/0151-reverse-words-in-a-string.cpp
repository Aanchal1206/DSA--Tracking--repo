
class Solution {
public:
    string reverseWords(string s) {

        stringstream ss(s);
        string word;
        vector<string> words;

        while (ss >> word) {
            words.push_back(word);
        }

        int left = 0;
        int right = words.size() - 1;

        while (left < right) {
            swap(words[left], words[right]);
            left++;
            right--;
        }

        string answer = "";

        for (int i = 0; i < words.size(); i++) {

            if (i > 0) {
                answer += " ";
            }

            answer += words[i];
        }

        return answer;
    }
};

