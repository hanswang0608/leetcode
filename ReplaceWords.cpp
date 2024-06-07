#include <string>
#include <vector>
#include <set>

using namespace std;

class Solution
{
public:
    string replaceWords(vector<string> &dictionary, string sentence)
    {
        vector<string> words;
        string word;
        for (auto const &c : sentence)
        {
            if (c == ' ')
            {
                words.push_back(word);
                word = "";
                continue;
            }
            word += c;
        }
        if (word != "")
        {
            words.push_back(word);
        }

        set<string> dict(dictionary.begin(), dictionary.end());
        string output = "";
        for (auto const &word : words)
        {
            string current = "";
            for (auto const &c : word)
            {
                current += c;
                if (dict.find(current) != dict.end())
                {
                    break;
                }
            }
            output += current + " ";
        }

        output.pop_back();

        return output;
    }
};