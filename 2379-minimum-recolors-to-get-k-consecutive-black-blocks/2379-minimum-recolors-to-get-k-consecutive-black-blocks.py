class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_c = 0
        for i in range(k):
            if blocks[i] == 'W':
                w_c+=1
        ans = w_c
        for i in range(1,len(blocks)-k+1):
            if blocks[i+k-1] == "W":
                w_c+=1
            if blocks[i-1] == "W":
                w_c-=1
            ans = min(ans,w_c)
        return ans