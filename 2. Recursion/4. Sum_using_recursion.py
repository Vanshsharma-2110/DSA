#--------------------xx BRUTE FORCE METHOD xx---------------------#
# def sum_rec(num):
#     total=0
#     for i in range(1,num+1):
#         total+=i
#     return total
# num = int (input("enter the Number: "))
# print(f"the sum of first {num} natural numbers is {sum_rec(num)}")


#--------------------xx Using Formula : [(N*(n+1))//2] --xx---------------------#
# def sum_rec(num):
#     return (num * (num + 1)) // 2
# num = int (input("enter the Number: "))
# print(f"the sum of first {num} natural numbers is {sum_rec(num)}")

#--------------------xx Using Recursion xx----------------------------#

def recursion(num):
   #base condition
    if num <= 1:
        return 1
    # Recursive case: current number + sum of previous numbers
    return num + recursion(num-1)
num = int (input("enter the Number: "))
print(f"the sum of first {num} natural numbers is {recursion(num)}")
