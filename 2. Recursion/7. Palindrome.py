def palindrome(i,str):
#---------xx Filtering string  xx---------------- 
    # this filter out all the non alphanumeric characters so we can use it 
    str = "".join(filter(lambda c: c.isalnum(),str))
    # this converst the entire string to lower case so the data is uniform
    str = str.lower()
    
#-----------xx Main logic xx---------------- 
    # BASE CONDITION: if i exceeds half of string , all element have been compared and are true 
    # ,then return true
    
    if i >= len(str)//2:
        return True
    
    if str[i]!=str[len(str)-i-1]:
        return False
    return palindrome(i+1,str)


test_case1 = "TAKE U FORWARD"
test_case2 ="ABCDCBA"
test_case3 ="A man, a plan, a canal: Panama"
print(f"Is The Test_case1 a palindrome? {palindrome(0,test_case1)}")
print(f"Is The Test_case2 a palindrome? {palindrome(0,test_case2)}")
print(f"Is The Test_case3 a palindrome? {palindrome(0,test_case3)}")