def recursion(current,num):
    if current>num:
        return
    print(current,end=" ")
    recursion(current+1,num)

num = int (input("enter the Number: "))
recursion(1,num)
