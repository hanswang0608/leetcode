class Solution {
  int removeDuplicates(List<int> nums) {
    int i = 0;
    for (var num in nums) {
      if (num != nums[i]) {
        i++;
        nums[i] = num;
      }
    }
    return i + 1;
  }
}
