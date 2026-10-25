class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        
        expected=sorted(heights)
        
        output=0

        check=list(zip(expected,heights))
        
        for exp,hei in check:
            if exp!=hei:
                output+=1

        return output        