class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        s=[]
        for i in A:
            l=[]
            for j in i[::-1]:
                l+=[0 if j==1 else 1]
            s+=[l]
        return s
        