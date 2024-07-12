class Solution {
  int removeElement(List<int> nums, int val) {
    int count = 0;
    for (var n in nums) {
      if (n != val) {
        nums[count] = n;
        count++;
      }
    }
    return count;
  }
}
