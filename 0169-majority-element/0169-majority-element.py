class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq ={}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        for key ,value in freq.items():
            if value > len(nums)//2:
                return key