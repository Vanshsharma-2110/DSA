import math

class Solution:
    def findGCD(self,num1, num2):

#------------xx-BRUTE FORCE-x----------------#
        # gcd = 1
        # for i in range(1,min(num1,num2)+1):
        #     if(num1%i == 0 and num2%i == 0):
        #         gcd = i
        # return(gcd)

        #! OPTIMAL - euclidian formula:
        #* gcd(a,b) = gcd(a-b,b) given a>b
        # ! OR
        #*  The GCD of two numbers doesn't change if you replace the larger number
        #*  with the remainder when divided by the smaller number.

        while(num1 > 0 and num2 > 0):
            if(num1 > num2):
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        if(num1 == 0): return num2
        return num1

num1 = int(input("enter num1:"))
num2 = int(input("enter num2:"))
sol = Solution()

print("greatest common divisor from ",num1 ,"and", num2, "is:", sol.findGCD(num1,num2))