class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        s = lambda x : x*x
        A = list(map(s,A))
        A.sort()
        return A