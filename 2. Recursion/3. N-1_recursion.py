def recursion(current):
    if current<1:
        return
    print(current,end=" ")
    recursion(current-1)

num = int (input("enter the Number: "))
recursion(num)
