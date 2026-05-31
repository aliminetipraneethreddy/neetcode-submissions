class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=[]
        for i in range(len(heights)):
            if heights[left]<heights[left+1]:
                lrft=left+1
            if heights[right]<heights[right-1]:
                right=right-1
            maxarea.append(max(heights[left],heights[left])*(left-right))
        return max(maxarea)

        