def printDivisors(n):
    num = n
    d = []
    for i in range (num,0,-1):
        if num%i==0:
            d.append(i)
    d.reverse()
    return d

num = int(input("Enter your number: "))
print( f"ALL Devisor of {num} are {printDivisors(num)}")