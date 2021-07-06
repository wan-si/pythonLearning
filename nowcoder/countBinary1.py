while True:
    try:
        num = int(input())
        # print(num.to_bytes)
        print(str('{0:b}'.format(num)).count('1'))
    except:
        break