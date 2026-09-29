class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count =0
        seen = {}
        if len(s)<3:
            return 0
        for i in range(3):
            seen[s[i]] = seen.get(s[i],0)+1
        if len(seen)==3:
            count+=1
        for i in range(1,len(s)-3+1):
            seen[s[i+3-1]] = seen.get(s[i+3-1],0)+1
            seen[s[i-1]]-=1
            if seen[s[i - 1]] == 0:
                del seen[s[i - 1]]
            if len(seen) == 3:
                count += 1
        return count