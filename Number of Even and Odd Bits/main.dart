class Solution {
  List<int> evenOddBit(int n) {
    var output = [0, 0];
    for (int i = 0; i < 32; i++) {
      if (n & 1 == 1) {
        if (i % 2 == 0) {
          output[0]++;
        } else {
          output[1]++;
        }
      }
      n >>= 1;
    }
    return output;
  }
}
