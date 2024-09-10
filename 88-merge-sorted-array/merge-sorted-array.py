class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        x=0
        temp=[]
        while i<m and j<n:
            if(nums1[i]<=nums2[j]):
                temp.append(nums1[i])
                x+=1
                if i<m:
                    i+=1
            elif (nums1[i]>nums2[j]):
                temp.append(nums2[j])
                x+=1
                if j<n :
                    j+=1
        while i<m:
            temp.append(nums1[i])
            i+=1
        while j<n:
            temp.append(nums2[j])
            j+=1
        for k in range(m + n):
            nums1[k] = temp[k]
        