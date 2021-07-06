while True:
    try:
        beg=0
        lst = []
        m = int(input())
        for i in range(1,m*m*m+1,2):
            if m*m*m == (i+i+(m-1)*2)*m/2:
                beg = i
                break
        for i in range(m):
            odds = str(beg+2*i)
            lst.append(odds)
        if len(lst) == 1:
            print(str(lst[0]))
        else:
            print("+".join(lst))
    except:
        break