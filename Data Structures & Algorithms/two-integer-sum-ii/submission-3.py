class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        result=[]
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target and i<j:
                    result.append(i+1)
                    result.append(j+1)
                    break
        return result