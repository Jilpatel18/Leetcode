# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ans = []
        left , right = 0 ,mountainArr.length()-1
        while left<right:
            mid = left+(right-left)//2
            if mountainArr.get(mid) < mountainArr.get(mid+1):
                left = mid+1
            else:
                right = mid
        high = left
        left,right = 0,high
        while left<=right:
            mid = left+(right-left)//2
            if mountainArr.get(mid)== target:
                return mid
            elif mountainArr.get(mid) > target:
                right = mid-1
            else:
                left = mid+1
        left,right = high+1,mountainArr.length()-1
        while left<=right:
            mid = left+(right-left)//2
            if mountainArr.get(mid) == target:
                return mid
            elif mountainArr.get(mid) > target:
                left = mid+1
            else:
                right = mid-1
        return -1