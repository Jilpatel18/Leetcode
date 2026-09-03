impl Solution {
    pub fn uniform_array(nums1: Vec<i32>) -> bool {
        let min_val = *nums1.iter().min().unwrap();
        if min_val %2 !=0{
            return true;
        }
        nums1.iter().all(|&x|  x%2==0)
            }
}