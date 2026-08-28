class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zc =0
        # seen = set()
        best =0
        for i in range(len(nums)):
            # seen.add(nums[i])
            if nums[i] ==0:
                zc+=1
            while zc>k:
                if nums[left] == 0:
                    zc-=1
                left+=1
            best = max(best , i-left+1 )
        return best