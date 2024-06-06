#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        auto iter = s.rbegin();
        while (iter != s.rend() && *iter == ' ')
        {
            iter = next(iter);
        }

        int count = 0;
        while (iter != s.rend() && *iter != ' ')
        {
            iter = next(iter);
            count++;
        }

        return count;
    }
};

int main()
{
    Solution sol;
    string s = "Hello World";
    cout << sol.lengthOfLastWord(s) << endl;
}