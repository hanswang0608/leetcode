#include <vector>

using namespace std;

class Solution
{
public:
    void sortColors(vector<int> &nums)
    {
        vector<int> count{0, 0, 0};
        for (auto const &num : nums)
        {
            count[num]++;
        }
        int i = 0;
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < count[j]; k++)
            {
                nums[i] = j;
                i++;
            }
        }
    }
};