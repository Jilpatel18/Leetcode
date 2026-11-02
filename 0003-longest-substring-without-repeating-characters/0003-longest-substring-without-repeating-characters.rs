impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut max_len = 0;
        let mut left =0;
        for i in 0..chars.len(){
            while chars[left..i].contains(&chars[i]){
                left+=1;
            }
            
            let current_len = i - left + 1;
            max_len = max_len.max(current_len);
        }
        max_len as i32
    }
}