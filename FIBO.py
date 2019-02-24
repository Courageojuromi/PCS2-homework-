def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, b+a
    return a

if __name__ == "__main__":
    print fib(25)