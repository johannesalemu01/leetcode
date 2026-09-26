class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:

        newS=[]
        tempS=[]
        key=""
        kdg={}

        for key,value in knowledge:
          kdg[key]=value 



        for char in s:
            if char=="(":
                newS.extend(tempS)
                tempS=[]
            elif char ==")":
                key="".join(tempS)
                if key in kdg:
                    newS.append(kdg[key])

                else:
                    newS.append("?")

                tempS=[]
                     
            else:
                tempS.append(char)
            
        newS.extend(tempS)

        return "".join(newS)    




                    