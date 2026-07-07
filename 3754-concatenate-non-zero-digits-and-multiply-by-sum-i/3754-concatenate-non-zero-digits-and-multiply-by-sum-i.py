class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ''
        sumo =0
        for i in str(n):
            if i!= '0':
                s+=i
                sumo+=int(i)
        if s=='':
            return 0
        return int(s)*sumo