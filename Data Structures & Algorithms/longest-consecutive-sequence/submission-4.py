class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        longest=0
        seq=set(nums)

        for num in nums:
            if (num-1) not in seq:
                length=0
                while (num+length) in seq:
                    length+=1
                longest=max(length,longest)
        return longest