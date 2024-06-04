use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut count: HashMap<char, i32> = HashMap::new();
        for c in s.chars() {
            count.entry(c).and_modify(|v| *v += 1).or_insert(1);
        }
        
        let mut output = 0;
        let mut foundOdd = 0;
        for (k, v) in count.into_iter() {
            if v % 2 == 1 {
                foundOdd = 1;
            }
            output += v - v % 2;
        }

        return output + foundOdd;
    }
}