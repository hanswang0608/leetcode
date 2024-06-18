#include <math.h>
class Solution {
public:
    bool judgeSquareSum(int c) {
        int a = 0;
        int b = sqrt(c);
        if (b*b == c) return true;
        while (a <= c && b >= 0) {
            unsigned int val = pow(a, 2) + pow(b, 2);
            if (val == c) {
                return true;
            }
            else if (val < c) {
                a++;
            } else if (val > c) {
                b--;
            }
        }
        return false;
    }
};