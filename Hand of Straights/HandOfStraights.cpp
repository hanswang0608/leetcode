#include <vector>
#include <algorithm>
#include <unordered_map>
#include <map>
#include <iostream>

using namespace std;

class Solution
{
public:
    bool isNStraightHand(vector<int> &hand, int groupSize)
    {
        if (hand.size() % groupSize != 0)
        {
            return false;
        }

        map<int, int> count;
        for (auto const &card : hand)
        {
            count[card]++;
        }

        auto iter = count.begin();
        while (iter != count.end())
        {
            while (iter->second > 0)
            {
                iter->second--;
                int i = iter->first + 1;
                while (i < (iter->first + groupSize))
                {
                    if (count[i] > 0)
                    {
                        count[i]--;
                    }
                    else
                    {
                        return false;
                    }
                    i++;
                }
            }
            iter = next(iter);
        }

        return true;
    }
};

int main()
{
    Solution s;
    vector<int> hand{66, 75, 4, 37, 92, 87, 68, 65, 58, 100, 97, 42, 19, 66, 73, 1, 5, 44, 30, 29, 76, 31, 12, 35, 26, 93, 9, 36, 90, 16, 86, 15, 4, 9, 13, 98, 10, 14, 18, 90, 89, 3, 10, 65, 24, 31, 43, 25, 54, 55, 54, 81, 10, 80, 31, 12, 15, 14, 59, 27, 64, 93, 32, 26, 69, 79, 13, 32, 29, 24, 27, 91, 92, 82, 37, 101, 100, 61, 74, 30, 91, 62, 36, 92, 28, 23, 4, 63, 55, 3, 11, 11, 101, 22, 34, 25, 2, 75, 43, 72};
    cout << s.isNStraightHand(hand, 2) << endl;
}