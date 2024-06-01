class Solution {
  int scoreOfString(String s) {
    int sum = 0;
    for (int i = 1; i < s.length; i++) {
      sum += (s[i].codeUnitAt(0) - s[i - 1].codeUnitAt(0)).abs();
    }
    return sum;
  }
}
