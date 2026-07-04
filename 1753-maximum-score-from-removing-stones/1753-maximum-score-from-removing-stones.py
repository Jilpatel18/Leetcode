class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        total = a + b + c
        maxPile = max(a, b, c)
        return min(total // 2, total - maxPile)