class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=1
        while right>left:
            maxarea1=min(right,left)*(left-right)
            if heights[right]<heights[right-1]:
                right+=1
            if heights[left]<heights[left+1]:
                left-=1
            if maxarea1>maxarea:
                maxarea=maxarea
        return maxarea

        