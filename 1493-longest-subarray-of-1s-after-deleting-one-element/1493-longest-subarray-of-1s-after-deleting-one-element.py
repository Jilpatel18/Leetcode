class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        length =0 
        left =0
        count =0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            while count > 1:
                if nums[left]==0:
                    count -= 1
                left+=1
            length = max(length,i-left+1)
        return length-1