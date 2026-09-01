impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max = 0;
        for i in 0..prices.len()-1{
            let ans = prices[i+1]-prices[i];
            if ans>0{
                max+=ans;
            }
        }
        max
    }
}