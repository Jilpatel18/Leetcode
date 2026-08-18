class Solution:
    def rotate(self,s:str,k:int):
        k%=len(s)
        return s[k:]+s[:k]
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for k in range(len(s)):
            if self.rotate(s,k) == goal:
                return True
        return False
