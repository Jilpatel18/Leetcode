class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        max_d = 0
        i,j=0,0
        while i<len(nums1) and j < len(nums2):
            if nums1[i]> nums2[j]:
                i+=1
            else:
                max_d = max(max_d,j-i)
                j+=1
                
        return max_d

