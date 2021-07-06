# 描述
# 将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。


# 输入描述：
# 输入一个字符串，可以有空格

# 输出描述：
# 输出逆序的字符串

while True:
    try:
        string = input()
        print(string[::-1])
    except:
        break