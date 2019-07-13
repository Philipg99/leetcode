class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d={}
        c=0
        for i in J:
            d[i]=1
        for i in S:
            if d.get(i,0):
                c+=1
        return c
            

            