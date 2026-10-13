class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.lower()

        title_list=title.split(" ")
        
        result=[]

        for word in title_list:
            if len(word)<3:
                result.append(word)
            else:
                result.append(word.capitalize()) 
                
        return " ".join(result)
