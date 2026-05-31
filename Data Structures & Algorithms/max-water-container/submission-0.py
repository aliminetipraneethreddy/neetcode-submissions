class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(height)-1
        for i in range(len(height)):
            if height[left]<height[left+1]:
                lrft=left+1
            if height[right]<height[right-1]:
                right=right-1
        area=height[left]*height[right]
        return area

        