import 'dart:math';

class Solution {
  int findPoisonedDuration(List<int> timeSeries, int duration) {
    int count = duration;
    for (int i = 0; i < timeSeries.length - 1; i++) {
      count += min(duration, timeSeries[i + 1] - timeSeries[i]);
    }
    return count;
  }
}
