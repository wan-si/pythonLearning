# 找出给定字符串中大写字符(即'A'-'Z')的个数

while True:
    try:
        string = input()
        count =0
        for i in string:
            if i.isupper():
                count+=1
        print(count)
    except:
        break    