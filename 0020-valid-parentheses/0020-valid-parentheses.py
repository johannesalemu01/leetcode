class Solution:
    def isValid(self, s: str) -> bool:
        checkParentheses={
            "(":")",
            "{":"}",
            "[":"]",
            }

        parenthesesList=[]

        for parantheses in s:
            if parantheses in '([{':
                parenthesesList.append(parantheses)
            else:
                if not parenthesesList:
                    return False
                open_key=parenthesesList.pop()
                if checkParentheses[open_key]!=parantheses:
                    return False

        return not parenthesesList                    
