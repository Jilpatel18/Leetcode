class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left =0
        best =0
        seen = {}
        for right,num in enumerate(fruits):
            seen[num] = seen.get(num,0)+1
            while len(seen)>2:
                seen[fruits[left]]-=1
                if seen[fruits[left]] ==0 :
                    del seen[fruits[left]]
                left+=1
            best = max(best,right-left+1)
        return best