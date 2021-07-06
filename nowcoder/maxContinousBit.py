while True:
    try:
        num = int(input())
        numb = str('{0:b}'.format(num))
        countList = []
        count = 0
        for i in str(numb):
            if i == '1':
                count += 1
            else:
                if count != 0:
                     countList.append(count)
                count = 0
        countList.append(count)
        print(max(countList))
    except:
        break    
