class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=0
        while right>left:
            maxarea1=min(right,left)*(right-left)
            if heights[left]<heights[right-1]:
                left+=1
            else:
                right-=1
            if maxarea1>maxarea:
                maxarea=maxarea1
        return maxarea

        