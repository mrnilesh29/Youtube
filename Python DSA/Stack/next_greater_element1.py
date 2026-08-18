class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0]*len(nums2) 
        st = []

        j = len(ans)-1
        for i in range(len(nums2)-1,-1,-1) : 
            while st and nums2[i] >= st[-1] : 
                st.pop() 
            if not st : 
                ans[j] = -1 
                st.append(nums2[i])
                j -=1 
            elif st[-1] > nums2[i] : 
                ans[j] = st[-1] 
                st.append(nums2[i])
                j-=1
            
        dic = {}
        j = 0 
        for i in range(len(nums2)) : 
            dic[nums2[i]] = ans[i] 

        ans2 = [0]*len(nums1)
        for i in range(len(nums1)) : 
            ans2[i] = dic[nums1[i]]

        return ans2 



        