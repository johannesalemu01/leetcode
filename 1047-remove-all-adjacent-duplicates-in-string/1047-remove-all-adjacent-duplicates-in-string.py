class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack=[]

        for char in s:
            if stack:
                if stack[-1]==char:
                    stack.pop()
                    continue
                else:
                    stack.append(char)
            else:
                stack.append(char)        

        print(stack)
        return "".join(stack)                