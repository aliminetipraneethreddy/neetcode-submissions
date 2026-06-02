class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=[]
        while right>left:
            maxarea.append(min(right,left)*(right-left))
            if heights[left]<heights[right-1]:
                left+=1
            else:
                right-=1
            
        return max(maxarea)

        