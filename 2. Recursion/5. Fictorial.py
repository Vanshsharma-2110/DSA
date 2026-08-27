def fict(n):
    if n <= 1:
        return 1
    return n*fict(n-1)

num = int (input( "Enter the number: "))
print (f" Fictorial of {num} is {fict(num)}")
