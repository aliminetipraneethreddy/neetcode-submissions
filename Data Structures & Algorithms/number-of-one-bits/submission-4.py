class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        n1=str(n)
        for i in n1 :
            if i=="1":
                count+=1
        return count
