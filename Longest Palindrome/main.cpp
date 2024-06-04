class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> m;
        for (char const &c: s) {
            m[c]++;
        }

        int output = 0;
        bool foundOdd = 0;
        for (auto const& [k, v]: m) {
            if (v % 2 == 1) {
                foundOdd = 1;
            }
            output += v - v % 2;
        }

        return output + foundOdd;
    }
};