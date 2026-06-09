class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        kmax=0
        k=1
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if nums[j+1]==nums[j]+1:
                    k+=1
            if kmax<k:
                kmax=k
            k=1
        return kmax+1
            
        
        