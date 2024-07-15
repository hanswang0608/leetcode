impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        let (mut even, mut odd) = (0, 0);
        let mut num = n;
        for i in 0..32 {
            if num & 1 == 1 {
                if i % 2 == 0 {
                    even += 1;
                } else {
                    odd += 1;
                }
            }
            num = num >> 1;
        }
        vec![even, odd]
    }
}
