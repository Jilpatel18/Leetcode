class Solution:
    def search(self,matrix,midR,target):
        low,high =0,len(matrix[0])-1
        while low<=high:
            mid = low+(high-low)//2
            if matrix[midR][mid] == target:
                return True
            elif matrix[midR][mid]>target:
                high = mid-1
            else:
                low = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowR , highR = 0,len(matrix)-1
        midR =-1
        while lowR <= highR:
            cols = len(matrix[0])-1
            midR = lowR + (highR-lowR)//2
            if matrix[midR][0] <= target <= matrix[midR][cols]:
                return self.search(matrix,midR,target)
            elif matrix[midR][0] < target:
                lowR = midR+1
            else:
                highR = midR-1
        return False