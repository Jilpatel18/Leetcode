class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = {}
        if len(p) > len(s):
            return []
        for i in range(len(p)):
            freq[p[i]] = freq.get(p[i],0)+1
        sfre = {}
        k = len(p)
        for i in range(k):
            sfre[s[i]] = sfre.get(s[i],0)+1
        ans =[]
        if sfre == freq:
            ans.append(0)
        
        for i in range(1,len(s)-k+1):
            out = s[i-1]
            sfre[out]-=1
            if sfre[out]==0:
                del sfre[out]
            sfre[s[i+k-1]] = sfre.get(s[i+k-1],0)+1
            if sfre == freq:
                ans.append(i)
        return ans