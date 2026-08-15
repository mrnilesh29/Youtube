
# def binary_search(arr, target, left=0, right=None):
#     if right is None : right = len(arr)-1
#     if left > right : return -1 
#     mid = (left+right)//2 
#     if arr[mid] == target : 
#         return mid 
#     elif arr[mid] < target :
#         return binary_search(arr,target , mid+1,right)
#     else : 
#         return binary_search(arr,target , left,mid-1) 
        
        
    


# # Test Cases
# print(binary_search([1, 3, 5, 7, 9], 7))       # Expected: 3
# print(binary_search([1, 3, 5, 7, 9], 4))       # Expected: -1
# print(binary_search([2, 4, 6, 8, 10], 2))      # Expected: 0
# print(binary_search([2, 4, 6, 8, 10], 10))     # Expected: 4
# print(binary_search([], 5))                     # Expected: -1