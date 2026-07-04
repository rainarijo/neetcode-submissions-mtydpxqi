class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        min=10000
        for i in range(n):
            if nums[i]<min:
                min=nums[i]
        return min