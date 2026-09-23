class Solution:
    def isHappy(self, n: int) -> bool:
        

        strNum=str(n)
        isNew=True
        checked=[]
        while isNew:
            if n in checked:
                return False
            sum=0
            strNum=str(n)

            for i in strNum:
                i=int(i)
                sum+=i*i
            if sum==1:
                return True    
            checked.append(n)
            n=sum

      


              



