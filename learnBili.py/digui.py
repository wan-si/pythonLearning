# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(8))

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,7):
    print(fib(i),end=' ')