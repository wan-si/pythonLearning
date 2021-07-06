# 把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。
# 数据范围：0<=m<=10，1<=n<=10。
# 本题含有多组样例输入。

def putApple(n,m):
    if n<1 or m<1:
        return 0
    elif n ==1 or m==1:
        return 1
    elif n<m:
        return putApple(n,n)    
    else:
        return putApple(n,m-1)+putApple(n-m,m)
while True:
    try:
        n,m= map(int,input().split())
        print(putApple(n,m))
    except:
        break    
        
