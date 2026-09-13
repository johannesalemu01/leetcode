class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr=str(x)
        reversed=xStr[::-1]

        if xStr==reversed:
            return True
        else:    
          return False            

