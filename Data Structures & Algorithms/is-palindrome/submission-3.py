from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace()
        for char in punctuation:
            s=s.replace(char,"")
        
        