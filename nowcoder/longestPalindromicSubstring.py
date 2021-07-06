# 描述
# 给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
# 所谓回文串，指左右对称的字符串。
# 所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
# （注意：记得加上while处理多个测试用例）

# 输入描述：
# 输入一个仅包含小写字母的字符串

# 输出描述：
# 返回最长回文子串的长度
while True:
    try:
        value = ''
        string = input()
        list= []
        for i in range(len(string)):
            for j in range(len(string)):
                value = string[i:len(string)-j:1]
                if value == value[::-1]:
                    list.append(len(value))
        print(max(list))
    except:
        break