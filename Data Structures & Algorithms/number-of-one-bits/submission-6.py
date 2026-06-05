class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        n1=str(n)
        return len(n1.replace('0',""))
