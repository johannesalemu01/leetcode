class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result=[]

        ptr_1=len(num1)-1
        ptr_2=len(num2)-1
        carry=0
        while ptr_1>=0 or ptr_2>=0 or carry:
            sum=0
            digit1 = int(num1[ptr_1]) if ptr_1 >= 0 else 0
            digit2 = int(num2[ptr_2]) if ptr_2 >= 0 else 0
                
            sum+=digit1+digit2+carry

            if sum>=10:
                carry=1
                result.append(str(sum-10))

            else:
                carry=0      
                result.append(str(sum))
          
            ptr_1-=1    
            ptr_2-=1    

        final_result= "".join(result)   
        return final_result[::-1]