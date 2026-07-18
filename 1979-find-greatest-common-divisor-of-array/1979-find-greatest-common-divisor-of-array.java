class Solution {
    public int Gcd(int a , int b){
        while (b!=0){
            int temp = a;
            a= b;
            b=temp%b;
        }
        return Math.abs(a);
    }
    public int findGCD(int[] nums) {
        int mn =Integer.MAX_VALUE;
        int mx = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>mx){
                mx = nums[i];
            }
             if(mn>nums[i]){
                mn = nums[i];
            }
        }
        return Gcd(mn,mx);
    }
}