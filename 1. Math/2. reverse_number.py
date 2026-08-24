def reverse_num(n):
    rev_n = 0
    while(n>0):
        ld = n%10
        rev_n = (rev_n*10)+ld
        n=n//10
    return rev_n
    
num = int(input("Enter the number: "))
rev_num = reverse_num(num)
print (f"The reverse of {num} is {rev_num}")