class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ","")
        s=s.replace('?',"")
        s=s.lower()
        a=[False]*len(s)
        for i in range(len(s)):
            if s[i]==s[-(i+1)]:
                a[i]=True
            else:
                a[i]=False
        if False in a:
            return False
        else:
            return True
