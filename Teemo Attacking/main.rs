impl Solution {
    pub fn find_poisoned_duration(time_series: Vec<i32>, duration: i32) -> i32 {
        let mut count = duration;
        for i in 0..time_series.len() - 1 {
            count += std::cmp::min(duration, time_series[i + 1] - time_series[i]);
        }
        return count;
    }
}
