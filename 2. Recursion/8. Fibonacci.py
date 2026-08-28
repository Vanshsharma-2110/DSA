def fibonacci(n):
    if n <= 1:
        return n
    last_term = fibonacci(n - 1)
    Second_last_term = fibonacci(n - 2)
    return last_term + Second_last_term

n = int(input("Enter the Value of N: "))
fibonacci(n)
