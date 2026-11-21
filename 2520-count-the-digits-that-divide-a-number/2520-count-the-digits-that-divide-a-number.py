class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        num_str=str(num)

        for digit in num_str:
            digit=int(digit)
            if num%digit==0:
                count+=1

        return count    
