#include <vector>
#include <iostream>

using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        vector<int> temp;
        int i = 0;
        int j = 0;
        while (i < m && j < n)
        {
            if (nums1[i] < nums2[j])
            {
                temp.push_back(nums1[i]);
                i++;
            }
            else
            {
                temp.push_back(nums2[j]);
                j++;
            }
        }
        if (i < m)
        {
            temp.insert(temp.end(), nums1.begin() + i, nums1.begin() + m);
        }
        if (j < n)
        {
            temp.insert(temp.end(), nums2.begin() + j, nums2.end());
        }

        nums1 = temp;
    }
};

int main()
{
    Solution s;
    vector<int> nums1{1, 2, 3, 0, 0, 0};
    vector<int> nums2{2, 5, 6};
    s.merge(nums1, nums1.size() - nums2.size(), nums2, nums2.size());
    for (auto const &e : nums1)
    {
        cout << e << endl;
    }
}