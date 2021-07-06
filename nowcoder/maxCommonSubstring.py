# 给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
# 注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串

while True:
    try:
        str1 = input()
        str2 = input()
        n = 0
        for i in range(len(str1)):
            if str1[i-n:i+1] in str2:
                n +=1
        print(n)
    except:
        break    
