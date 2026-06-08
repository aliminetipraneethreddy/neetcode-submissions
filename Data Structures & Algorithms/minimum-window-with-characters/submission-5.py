class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        arr=[]
        for i in range(len(s)):
            if s[i]in t:
                
                s1=s[i]
                for j in range(i+1,len(s)):
                    if s[j] in t:
                        s1=s1+(s[j])
                    else:
                        break
                arr.append(s1)
        ans=""
        for x in arr:
            flag=True
            for ch in t:
                if ch not in x:
                    flag = False
                    break
            if flag:
                if ans=="" or  len(x)<len(ans):
                    ans=x
        return ans

                

                



