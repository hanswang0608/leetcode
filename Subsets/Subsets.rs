impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut output: Vec<Vec<i32>> = vec![];
        fn dfs(nums: &Vec<i32>, path: Vec<i32>, output: &mut Vec<Vec<i32>>) {
            output.push(path.to_vec());
            if nums.len() == 0 {
                return;
            } else {
                for i in 0..nums.len() {
                    let mut path_copy = path.clone();
                    path_copy.push(nums[i]);
                    dfs(&nums[i + 1..].to_vec(), path_copy, output);
                }
            }
        }
        let mut path: Vec<i32> = vec![];
        dfs(&nums, path, &mut output);
        return output;
    }
}
