class Solution:
    def Gcd(this,a,b):
        while b!=0:
            a,b = b,a%b
        return abs(a)
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        c=  self.Gcd(a,b)
        return c