class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        for row in matrix:
            x = min(row)
            col = row.index(x)

            if x == max(r[col] for r in matrix):
                ans.append(x)

        return ans