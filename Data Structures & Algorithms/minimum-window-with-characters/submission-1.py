class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        arr=[]
        for i in range(len(s)):
            if s[i]in t:
                count=0
                s1=s[i]
                for j in range(i+1,len(s)):
                    if s[j] in t:
                        s1.append(s[j])
                    else:
                        break
                arr.append(s1)
        min_length=min(len(s) for s in s1)
                

                



