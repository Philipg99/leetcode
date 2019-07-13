class Solution:
    def toLowerCase(self, str: str) -> str:
        s=''
        for i in str:
            s+=i.lower()
        return s