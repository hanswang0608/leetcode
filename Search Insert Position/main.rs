impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = (nums.len() - 1) as usize;
        let mut mid: usize = 0;
        while l + 1 < r {
            mid = (r - l) / 2 + l;
            // println!("{}, {}, {}, {}, {}", mid, l, r, nums[mid], target);
            if (nums[mid] == target) {
                return mid as i32;
            }
            if (nums[mid] < target) {
                l = mid;
            }
            if (nums[mid] > target) {
                r = mid;
            }
        }
        return mid as i32;
    }
}
