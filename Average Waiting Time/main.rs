impl Solution {
    pub fn average_waiting_time(customers: Vec<Vec<i32>>) -> f64 {
        if customers.len() == 0 {
            return 0.0
        }
        
        let mut lastTime = customers[0][0] + customers[0][1];
        let mut curTime = 0;
        let mut total : f64 = (lastTime - customers[0][0]) as f64;

        for i in 1..customers.len() {
            if lastTime >= customers[i][0] {
                curTime = lastTime + customers[i][1];
            } else {
                curTime = customers[i][0] + customers[i][1];
            }
            total += (curTime - customers[i][0]) as f64;
            lastTime = curTime;
        }

        return total / customers.len() as f64;
    }
}