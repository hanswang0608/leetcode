#include <string>

using namespace std;

class Solution
{
public:
    int strStr(string haystack, string needle)
    {
        if (needle.length() > haystack.length())
        {
            return -1;
        }

        for (int i = 0; i < haystack.length(); i++)
        {
            for (int j = 0; j < needle.length(); j++)
            {
                if (i + j >= haystack.length())
                {
                    return -1;
                }
                if (haystack[i + j] != needle[j])
                {
                    break;
                }
                if (j + 1 == needle.length())
                {
                    return i;
                }
            }
        }

        return -1;
    }
};