impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i: usize = 0;
        for num in nums {
            if (*num != nums[i]) {
                i += 1;
                nums[i] = *num;
            }
        }
        return (i + 1) as i32;
    }
}
