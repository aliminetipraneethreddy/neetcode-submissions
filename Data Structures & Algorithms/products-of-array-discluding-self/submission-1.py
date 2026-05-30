class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[1]*n
        for i in range (len(nums)):
            prod=0
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    prod=prod*nums[j]
            a.append(prod)
        return prod

        