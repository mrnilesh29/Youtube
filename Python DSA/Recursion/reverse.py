def reverse_digit(n) :
    if n <= 10 : 
        return n 
    print(n%10,end="")
    return reverse_digit(n//10)


print(reverse_digit(12))