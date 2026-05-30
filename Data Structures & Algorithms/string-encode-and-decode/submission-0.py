class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        count=0
        for  i in strs:
            str1=str1 +str(len(i))+"#"+i
        return str1

            

    def decode(self, s: str) -> List[str]:
        str1=[]
        for i in range(len(s)):
            if s[i].isdigit():
                a=int(s[i])
                str1.append(s[i+2:i+2+a])
        return str1



