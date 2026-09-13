class Solution:
    def isPalindrome(self, x: int) -> bool:
       num_str=str(x)
       if num_str[0] == '-':
        res = [-int(num_str[1])] + [int(digit) for digit in num_str[2:]]
       else:
         res = [int(digit) for digit in num_str]
       left=0   
       right=len(num_str)-1 

       while left < right:
        if num_str[left]!=num_str[right]:
            return False
        left +=1
        right-=1

       return True     


  

