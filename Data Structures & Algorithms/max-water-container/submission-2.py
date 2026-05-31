class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=[]
        while left<right:
            maxarea.append(min(heights[left ],heights[right])*(right-left))
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        return max(maxarea)