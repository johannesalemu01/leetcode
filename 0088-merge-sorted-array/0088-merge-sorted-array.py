class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k=n+m-1
        for i in range(m-1,-1,-1):
            nums1[k]=nums1[i]
            k-=1
        k=n
        i=0 
        j=0
        while  j < n and k<n+m:
            if nums2[j] <= nums1[k]:
                nums1[i]=nums2[j]
                j+=1
            else:
                nums1[i]=nums1[k]  
                k+=1
            i+=1

        while j<n:
            nums1[i]=nums2[j]
            j+=1
            i+=1

        while k<n+m:
            nums1[i]=nums1[k]
            k+=1
            i+=1




       


               


        