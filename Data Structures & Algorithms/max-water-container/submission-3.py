class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)
        maxarea=1
        while right>left:
            maxarea1=min(right,left)*(left-right)
            if nums[right]<nums[right+1]:
                right+=1
            if nums[left]<nums[left-1]:
                left-=1
            if maxarea1>maxarea:
                maxarea=maxarea
        return maxarea

        