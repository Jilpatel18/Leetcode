class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res =[]
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                res.append(i)
        return res
