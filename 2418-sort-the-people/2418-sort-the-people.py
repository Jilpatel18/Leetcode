class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        disct = {}
        for i in range(len(names)):
            disct[heights[i]] = names[i]

        disct = dict(sorted(disct.items(), reverse=True))
        return list(disct.values())
