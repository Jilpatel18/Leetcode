impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars : Vec<char> = s.chars().collect();
        if chars.is_empty() {
    return true;
}
        let mut left =0;
        let mut right = chars.len()-1;
        while left< right{
            if !chars[left].is_alphanumeric(){
                left+=1;
                continue;
            }
            if !chars[right].is_alphanumeric(){
                right-=1;
                continue;
            }
            if !chars[left].eq_ignore_ascii_case(&chars[right]){
                return false;
            }
            left+=1;
            right-=1

        }
        true
    }
}