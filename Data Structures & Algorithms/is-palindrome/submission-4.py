from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        for char in punctuation:
            s=s.replace(char,"")
        left =0
        right=len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True


