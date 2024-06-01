public class Solution {
    public int ScoreOfString(string s) {
        int sum = 0;
        for (int i = 1; i < s.Length; i++) {
            sum += Math.Abs(s[i] - s[i-1]);
        }
        return sum;
    }
}