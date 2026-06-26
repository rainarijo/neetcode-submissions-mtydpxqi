class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","-","*","/"]

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                    
                    a=stack.pop()
                    b=stack.pop()

                    if tokens[i]=="+":
                        res=a+b
                    elif tokens[i]=="-":
                            res=b-a
                    elif tokens[i]=="*":
                        res=a*b
                    elif tokens[i]=="/":
                        res=int(b/a)
                    
                    stack.append(res)
        return stack[0]
                    
                        
