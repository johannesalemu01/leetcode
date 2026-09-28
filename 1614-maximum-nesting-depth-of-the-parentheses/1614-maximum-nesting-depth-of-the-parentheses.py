class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack=[]
        max_depth=0

        for i in s:
            if i =="(":
                stack.append(i)
                max_depth=max(len(stack),max_depth)
            elif i ==")":
                stack.pop()
                max_depth=max(len(stack),max_depth)
            else:
                continue
        return max_depth



