class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        s=[]
        for i in range(left,right+1):
            si=list(map(int,list(str(i))))
            flg=0
            for e in si:
                if e==0:
                    flg=1
                    break
                if i%e!=0:
                    flg=1
                    break
            if flg==0:
                s+=[i]
        return s
        