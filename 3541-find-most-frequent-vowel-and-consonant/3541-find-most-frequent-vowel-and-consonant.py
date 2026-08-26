class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel ="aeiou"
        v ={}
        c ={}
        for i in range(len(s)):
            if s[i] in vowel:
                v[s[i]] = v.get(s[i],0)+1
            else:
                c[s[i]] = c.get(s[i],0)+1
        total =0
        a = max(v.values(),default=0)
        b= max(c.values(),default=0)

        return a+b