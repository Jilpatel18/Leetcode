class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        k = len(s1)
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            need[s1[i]] = need.get(s1[i],0)+1
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i],0)+1
        if need == window:
            return True
        for i in range(1,len(s2)-k+1):
            out = s2[i-1]
            window[out]-=1
            if window[out]==0:
                del window[out]
            window[s2[i+k-1]] = window.get(s2[i+k-1],0)+1
            if window == need:
                return True
        return False
            