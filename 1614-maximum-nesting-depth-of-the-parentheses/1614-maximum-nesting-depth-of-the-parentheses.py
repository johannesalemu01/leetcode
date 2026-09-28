class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = open = 0
        for char in s:
            if char =="(":
                open += 1
            elif char ==")":
                open -= 1

            max_depth=max(open,max_depth)
            
        return max_depth



