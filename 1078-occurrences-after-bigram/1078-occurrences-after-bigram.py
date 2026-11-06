class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        txt_list=text.split(" ")
        left=0
        right=1
        result=[]
        
        while right<len(txt_list)-1:
            if txt_list[left]==first and txt_list[right]==second:
                result.append(txt_list[right+1])
                
            left+=1
            right+=1

        return result           
