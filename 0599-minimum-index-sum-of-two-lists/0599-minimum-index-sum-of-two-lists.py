class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        
        min_index=len(list1)+len(list2)

        string_index={}

        new_list=[]

        for i,word in enumerate(list1):
            string_index[word]=i

        for j,word in enumerate(list2):

            current_sum=0

            if word in string_index:
                current_sum+= j+string_index[word]
                if current_sum==min_index:
                    min_index=current_sum
                    new_list.append(word)
                elif current_sum< min_index:
                    new_list.clear()
                    min_index=current_sum
                    new_list.append(word)


        return  new_list  
                    

