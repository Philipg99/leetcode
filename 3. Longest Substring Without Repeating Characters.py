class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alph=[0]*128
        mx=0
        n=1
        for i in s:
            if alph[ord(i)]!=0:
                c=0
                for k in range(31,len(alph)):
                    if alph[k]!=0:
                        c+=1
                mx = max(c,mx)
                d=alph[ord(i)]
                for j in range(31,len(alph)):
                    if alph[j]<=d:
                        alph[j]=0
            alph[ord(i)]=n
            n+=1
        c=0
        for k in range(31,len(alph)):
            if alph[k]!=0:
                c+=1
        return max(c,mx)
        
        