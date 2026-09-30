class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left,w_sum,=0,0
        length =float('inf')
        for i in range(len(nums)):
            w_sum+=nums[i]
            while w_sum >= target :
                length = min(length,i-left+1)
                w_sum-=nums[left]
                left+=1
        return 0 if length == float('inf') else length