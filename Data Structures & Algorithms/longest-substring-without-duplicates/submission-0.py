class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sublen=[]
        for i in range(len(s)):
            count=0
            for j in (i+1,len(s)):
                if s[i]!=s[j]:
                    count+=1
                if s[i]==s[j]:
                    sublen.append(count)
                    break
        return max(sublen)

        