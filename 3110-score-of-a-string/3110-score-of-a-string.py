class Solution:
    def scoreOfString(self, s: str) -> int:
        left =0
        right=1
        sum=0
        while left<right and right < len(s):
            sum +=abs(ord(s[left])- ord(s[right]))
            left +=1
            right +=1
        return sum    
        