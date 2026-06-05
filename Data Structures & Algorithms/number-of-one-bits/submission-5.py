class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            rem=n%10
            if rem==1:
                count+=1
            n=n//10
        return count
