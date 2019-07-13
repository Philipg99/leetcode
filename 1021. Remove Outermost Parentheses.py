class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        l=0
        r=''
        for i in S:
            if i=='(': 
                if l!=0:
                    r+=i
                l+=1
            if i==')': 
                l-=1
                if l!=0:
                    r+=i

        return r
            