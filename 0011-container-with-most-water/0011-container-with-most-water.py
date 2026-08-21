class Solution:
    def maxArea(self, nums: List[int]) -> int:
        area = 0
        i,j = 0,len(nums)-1
        while i<j:
            real =1 
            if nums[i]<nums[j]:
                real = nums[i]*(j-i)
                i+=1
            else:
                real = nums[j]*(j-i)
                j-=1
            area = max(area,real)
        return area