class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        reverse_digits=digits[::-1]
        digits=[]
        mult=1
        for i in range(0,len(reverse_digits)):
            if i== 0:
                num+=reverse_digits[i]*mult+1
            else:
                num+=reverse_digits[i]*mult
            mult *=10
        print(num)
        num_str=str(num)
        for i in num_str:
            digits.append(int(i))
            
        return digits    



