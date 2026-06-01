class Solution:
    def isValid(self, s: str) -> bool:
        s=s.replace(" ","")
        a=[]
        if s[0]=='}' or s[0]==']' or s[0]==')':
            return False
        for ch in s:
            a.append(ch)
        for i in range(len(a)//2):
            if (s[i]=='{' and s[len(a)-i-1]=='}' ) or (s[i]=='[' and s[len(a)-1-i]==']') or (s[i]=='(' and s[len(a)-i-1]==')' ):
                continue
            else:
                return False
        return True
            
        