class Solution {
public:
    bool canPermutePalindrome(string s) {
        std::unordered_map<char, int> counter;

        for(auto ch : s) {
            counter[ch] += 1;
        }

        int odd_cnt = 0;

        for(auto& pair : counter) {
            if(pair.second % 2) odd_cnt++;
        }

        if(s.length() % 2 == 1) {
            if(odd_cnt == 1) return true;
            return false;

        } else {
            if(odd_cnt == 0) return true;
            return false;
        }
    }
};