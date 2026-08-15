# def second_smallest(arr):
#     small = float('inf')
#     ssmall = float('inf')
    
#     for i in range(len(arr)) : 
#         if arr[i] < small : 
#             ssmall = small 
#             small = arr[i]
#         elif arr[i] < ssmall and arr[i] != small : ssmall = arr[i]
#     return ssmall
    


# # Test Cases
# print(second_smallest([10, 5, 8, 20, 15]))   # Expected: 8
# print(second_smallest([4, 2, 2, 1, 7]))      # Expected: 2
# print(second_smallest([1, 2, 3]))            # Expected: 2
# print(second_smallest([-5, -2, -9, -1]))     # Expected: -5
