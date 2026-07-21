class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r=0,len(heights)-1
        max=-1

        while l<r:
            m=min(heights[l],heights[r])
            tot=m*(r-l)
            if tot>max:
                max=tot
            if heights[l]==m:
                l+=1
            elif heights[r]==m:
                r-=1
        return max