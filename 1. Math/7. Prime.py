def check_prime(num):
    n= num
    for i in range (n-1,1,-1):
        if n % i == 0:
            return  False
    return True

num = int(input("Enter the number: "))
print(f"Is {num} a Prime Number? --> {check_prime(num)}")