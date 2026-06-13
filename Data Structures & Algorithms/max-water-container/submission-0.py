class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        
        l,r=0,len(heights)-1
        max=-1
        
        while l<r:
            m=min(heights[l],heights[r])
            water= m* (r-l)
            if water>max:
                max=water
            if m==heights[l]:
                l+=1
            elif m==heights[r]:
                r-=1
        return max

        # max=-1
        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):

        #         water=min(heights[i],heights[j])*(j-i)
        #         if water>max:
        #             max=water
        # return max



        
