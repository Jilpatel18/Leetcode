class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =[]
        freq ={}
        for word in strs:
            key = tuple(sorted(word))
            freq.setdefault(key,[]).append(word)
        for key,val in freq.items():
            res.append(val)
        return res