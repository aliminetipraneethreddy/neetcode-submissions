class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sublen=[]
        if s=="":
            return 0
        for i in range(len(s)):
            count=0
            seen=set()
            for j in range(i,len(s)):
                if s[j] not in seen:
                    count+=1
                    seen.add(s[j])
                else:
                    break
                
            sublen.append(count)
        return max(sublen)

        