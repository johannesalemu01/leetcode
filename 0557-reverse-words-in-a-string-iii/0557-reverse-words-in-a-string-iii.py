class Solution:
    def reverseWords(self, s: str) -> str:

        str_list=s.split(" ")


        result=[]

        for word in str_list:
            result.append(word[::-1])

        str_result=" ".join(result) 

        return str_result 

        