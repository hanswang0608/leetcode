impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut count = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums[count] = nums[i];
                count += 1;
            }
        }
        return count as i32;
    }
}
