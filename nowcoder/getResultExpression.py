# 给定一个字符串描述的算术表达式，计算出结果值。
# 输入字符串长度不超过100，合法的字符包括”+, -, *, /, (, )”，”0-9”，字符串内容的合法性及表达式语法的合法性由做题者检查。本题目只涉及整型计算。
while True:
    try:
        string = input()
        print(eval(string))
    except:
        break    