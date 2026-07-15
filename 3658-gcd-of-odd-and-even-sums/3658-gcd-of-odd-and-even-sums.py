import math
class Solution:
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = 0
        even_sum = 0
        n=n*2
        for i in range(1,n+1):
            if i%2==0:
                even_sum+=1
            else:
                odd_sum+=1
        x = gcd(odd_sum,even_sum)
        return x
        