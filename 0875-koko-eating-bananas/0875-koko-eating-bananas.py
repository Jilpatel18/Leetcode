class Solution:
    def check(self, piles, mid,h):
        count =0
        for i in range(len(piles)):
            count+=math.ceil(piles[i]/mid)
        return count <=h
                

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1,max(piles)
        # ans  = max(piles)
        ans = 0
        while low<=high:
            mid = low+(high-low)//2
            if(self.check(piles,mid,h)):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans