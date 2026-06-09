class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxk=0
        for i in range(len(nums)-1):
            k=1
            for j in range(len(nums)-1):
                if nums[j+1]==nums[j]+1:
                    k+=1
            if k>kmax:
                kmax=k
        return kmax
            
        
        