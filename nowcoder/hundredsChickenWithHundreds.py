def getChickens(money):
    # jiWeng = 5
    # jiMu = 3
    # jiChu = 1/3
    money = 100
    for i in range(int(100/5)):
        for j in range(int(100/3)):
            for k in range(100):
                if (i+j+k == 100) and (5*i + 3*j + k/3 ==100):
                    print(i,j,k)
while True:
    try:
        i = int(input())
        getChickens(i)
    except:
        break        