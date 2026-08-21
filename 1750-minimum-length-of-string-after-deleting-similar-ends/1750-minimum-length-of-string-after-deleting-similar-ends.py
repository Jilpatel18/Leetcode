class Solution:
    def minimumLength(self, s: str) -> int:
        
        while len(s)>1 and s[0] == s[-1]:
            pre = ""
            suf = ""
            i=0 
            j= len(s)-1
            x = s[0]
            if s[i] == s[j]:
                while i < len(s) and s[i] == x:
                    pre+=s[i]
                    i+=1
                while j >= 0 and s[j] == x:
                    suf=s[j]+suf
                    j-=1
            s = s.removeprefix(pre).removesuffix(suf)
        return len(s)