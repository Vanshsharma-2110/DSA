def checkArmstrong(n):
    num = n
    nums=[]

    while num>0:
        nums.append(num%10)
        num//= 10
    nums.reverse()

    power = len(nums)
    total = 0
    for i in nums:
        total += (i**power)

    return n==total

num = int (input("Enter the Number : "))
if checkArmstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")