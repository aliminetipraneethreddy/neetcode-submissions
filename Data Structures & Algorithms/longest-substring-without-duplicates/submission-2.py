class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sublen=[]
        for i in range(len(s)):
            count=1
            for j in range(i+1,len(s)):
                if s[i]!=s[j]:
                    count+=1
                if s[i]==s[j]:
                    sublen.append(count)
                    break
                else:
                    sublen.append9count
        return max(sublen)

        