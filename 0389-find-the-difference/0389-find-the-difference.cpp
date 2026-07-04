class Solution {
public:
    char findTheDifference(string s, string t) {
        map<char, int> cnt;

        for(auto ch : t) {
            cnt[ch] += 1;
        }

        for(auto ch : s) {
            cnt[ch] -= 1;
        }

        for(auto pair : cnt) {
            if(pair.second > 0) return pair.first;
        }

        return ' ';
    }
};