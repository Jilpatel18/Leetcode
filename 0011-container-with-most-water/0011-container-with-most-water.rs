impl Solution {
    pub fn max_area(nums: Vec<i32>) -> i32 {
        let mut area = 0;
        let mut left =0;
        let mut right = nums.len()-1;
        while left < right {
            let mut real =1;
            if nums[left] < nums[right]{
                real = nums[left]*((right-left) as i32);
                left+=1;
            }else{
                real = nums[right]*((right-left) as i32);
                right-=1;
            }
            area = area.max(real);
        }
        area
    }
}