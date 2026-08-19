class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        ans =[]
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0)+1
        sort = dict(sorted(freq.items(),key = lambda item:item[1],reverse = True))
        count =0
        for key,value in sort.items():
            if count == k:
                break
            ans.append(key)
            count+=1
        return ans