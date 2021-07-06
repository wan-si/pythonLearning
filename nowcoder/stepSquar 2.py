# 描述
# 请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

# 本题含有多组样例输入。
# 输入描述：
# 每组样例输入两个正整数n和m，用空格隔开。(1≤n,m≤8)

# 输出描述：
# 每组样例输出一行结果

# 示例1
# 输入：
# 2 2
# 1 2
# 复制
# 输出：
# 6
# 3
# 复制
def steps(n,m):
    if n==0 or m==0:
        return 1
    else:
        return steps(m,n-1)+steps(n,m-1)

while True:
    try:
        n,m = map(int,input().split())
        print(steps(n,m))
    except:
        break