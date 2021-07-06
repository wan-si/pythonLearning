import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    users = []
    total = 0
    min = 0
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        users.append(values)
    if n<0:
        print(0)
    elif n == 1:
        print(min(users[0]))
    else:
        list = []
        values = 0
        for i in range(n-1):
            temp= users[i]
            if i+1<n:
               values += min(temp)
               j = users[i].index(min(temp))
               temp = users[i+1]
               temp.remove[temp[j]]
               
               
               
  
                