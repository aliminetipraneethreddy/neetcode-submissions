class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        l=False
        for i in nums:
            if i==0:
                l=True
        if l==True:
            return list(nums[0],nums[1],nums[2])
        for i in range(len(nums)):
            sum=1
            for j in range (i+1,len(nums)-1):
                sum=nums[i]+nums[j]+nums[j+1]
                if sum==0:
                    k=[]
                    k.append(nums[i])
                    k.append(nums[j])
                    k.append(nums[j+1])
                    a.append(k)
                else:
                    continue
        return a


        