#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        int carry = 1;
        int i = digits.size() - 1;
        while (carry && i >= 0)
        {
            int temp = digits[i] + carry;
            digits[i] = temp % 10;
            carry = temp >= 10 ? 1 : 0;
            i--;
        }

        if (carry)
        {
            digits.insert(digits.begin(), 1);
        }

        return digits;
    }
};

int main()
{
}