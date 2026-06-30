class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        hmap = {}

        for i in range(m):
            for j in range(n):
                key = i+j
                if key not in hmap:
                    hmap[key] =[]
                hmap[key].append(mat[i][j])
        ans = []
        for d in range(m+n-1):
            if d % 2 ==0:
                ans.extend(hmap[d][::-1])
            else:
                ans.extend(hmap[d])
        return ans