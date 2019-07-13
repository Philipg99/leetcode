class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d={}
        for i in A:
            d[i]=d.get(i,0)+1
            if d[i]>1:
                return i