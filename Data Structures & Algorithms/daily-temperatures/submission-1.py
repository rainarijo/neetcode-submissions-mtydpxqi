class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]

        for i , t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackI=stack.pop()
                res=i-stackI
                result[stackI]=res
            stack.append((t,i))
        return result
