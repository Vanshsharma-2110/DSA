def isPalindrome(n):
    num = n
    rev_n = 0
    while(n>0):
        ld = n%10
        rev_n = (rev_n*10)+ld
        n=n//10
    return rev_n ==num
    
num = int(input("Enter the number: "))
print (f"Is {num} palindrome ?", isPalindrome(num))