class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        le=[]
        lo=[]
        for i in A:
            if i%2==0:
                le+=[i]
            else:
                lo+=[i]
        return le+lo