class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        result=[]
        nums2_dict={}
        left=0
        right=1

        while right < len(nums2):
            if nums2[left]>nums2[right]:
                if right==len(nums2)-1:
                    nums2_dict[nums2[left]]=-1
                    left+=1
                    right=left+1
                else:    
                    right+=1  
            elif nums2[left]<nums2[right]:
                nums2_dict[nums2[left]]=nums2[right]
                left+=1
                right=left+1
                
        nums2_dict[nums2[-1]] = -1        

        for num in nums1:
            result.append(nums2_dict[num])   

        return result         


            


 

       






