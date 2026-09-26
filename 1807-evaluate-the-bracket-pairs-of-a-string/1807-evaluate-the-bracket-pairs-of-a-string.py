class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        newS=""
        tempS=""

        kdg={}

        for key,value in knowledge:
          kdg[key]=value 



        for char in s:
            if char=="(":
                newS+=tempS
                tempS=""
            elif char ==")":
                if tempS in kdg:
                    newS+=kdg[tempS]

                else:
                    newS+="?" 

                tempS=""
                     
            else:
                tempS+=char
            
        newS+=tempS

        return newS    




                    