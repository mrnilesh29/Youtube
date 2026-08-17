class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        window_sum = 0 
        for i in range(k): 
            window_sum += arr[i]
        
        maxx = window_sum 
        i = 0 
        j = k 
        while j < len(arr) : 
            window_sum += arr[j] 
            window_sum -= arr[i]
            
            maxx = max(maxx , window_sum)
            i+=1 
            j+=1 
        return maxx / k

obj = Solution()
print(obj.maxSubarraySum([1,12,-5,-6,50,3],k=4))