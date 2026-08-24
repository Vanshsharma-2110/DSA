import math
def count_digit(n):
#-------xx BRUTE FORCE METHOD xx-------#
    # count = 0
    # while (n>0):
    #     ld = n%10
    #     count = count+1
    #     num= num//10
    # return count
    
    count = int (math.log10(n)+1)
    return count
    
n = int (input ("Enter the number: "))
count = count_digit(n)  
print ("Total digit in a number" ,count)  
