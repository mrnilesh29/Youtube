# a = [19,20,21,22] 
# print(type(a))

# b = [10,20,30,40,50]
# print(b[0])
# print(b[1])
# b[0] = 100
# print(b)
# print(b[-1])

# # N = "Nature"
# # print(N[0])
# # N[0] = "T"


# c = [1,1,1,1,1]
# print(c)

# print(b[3])
# print(b[3])
# print(b[3])
# print(b[3])
# print(b[3])

# A = [1,1.4,"Nilesh" , print() ,True ]
# print(A)

# B = [1,2,3,4,5,6]
# print(B)



# for i in range(0,len(a),1): 
#     print(a[i])


# for i in a : 
#     print(i)


# a = [1,2,3,4,5,6,7,7,7]
# a.append(20)
# a.append(100)
# a.insert(1,1000)
# a.extend([10,20,30])
# a.remove(5)
# a.sort()
# a.reverse()


# print(a.count(7))
# print(a.index(10))
# print(a.pop(1))

# b = a 
# print(a)

# print(b)
# b[0] = 500
# print(b)
# print(a)

# c = a.copy()
# print(c)
# print(a)
# c[0] = 500 
# print(a)
# print(c)

# l = [1,-2,-3,4,5,-6,7,-8,9]
# for i in range(len(l)): 
#     if l[i] < 0 : 
#         print(l[i])
#     else : 
#         continue 

# for i in range(len(l)): 
#     if l[i] > 0 : 
#         print(l[i])

# l = [10,20,30,40,50,60]
# s = 0 

# for i in l : 
#     s +=  i   

# mean = s / len(l)
# print(mean)



# l = [10,20,46,32,21,34,100,32]
# maxx = l[0]

# for i in range(len(l)): 
#     if l[i] > maxx : 
#         maxx = l[i]
        
# print(maxx)

        
        

# l = [10,20,46,32,21,34,100,32]
# maxx = l[0]
# smax = l[0]

# for i in range(len(l)): 
#     if l[i] > maxx : 
#         smax = maxx 
#         maxx = l[i]
        
#     elif l[i] > smax : 
#         smax = l[i]
        
# print(maxx)
# print(smax)


l = [1,1]

for i in range(0,len(l)-2,1): 
    if l[i] >  l[i+1] :
        print("not sorted")
        break
    
print("sorted") 
        
    

print(l)