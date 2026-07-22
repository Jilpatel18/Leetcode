class Solution:
    def check(self,arr,days,mid):
        count = 1
        total = 0
        for num in arr:
            if total+num>mid:
                count+=1
                total = 0
            total+=num
        return count <= days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low,high = max(weights),sum(weights)
        ans =0
        while low<=high:
            mid = low+(high-low)//2
            if(self.check(weights,days,mid)):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans