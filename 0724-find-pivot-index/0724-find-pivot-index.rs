impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let tot : i32 = nums.iter().sum();
        let mut left_sum = 0 ;
        for i in 0..nums.len(){
            let right_sum = tot-left_sum-nums[i];
            if left_sum == right_sum{
                return i as i32;
            }
            left_sum+=nums[i];
        }
        -1
    }

}