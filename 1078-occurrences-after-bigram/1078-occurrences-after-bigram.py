class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        txt_list=text.split(" ")
        left=0
        right=1
        result=[]

        for i in range(len(txt_list) - 2):
            if txt_list[i] == first and txt_list[i + 1] == second:
                result.append(txt_list[i + 2])

        return result           
