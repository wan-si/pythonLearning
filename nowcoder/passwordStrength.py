# 密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

# 一、密码长度:

# 5 分: 小于等于4 个字符

# 10 分: 5 到7 字符

# 25 分: 大于等于8 个字符

# 二、字母:

# 0 分: 没有字母

# 10 分: 全都是小（大）写字母

# 20 分: 大小写混合字母

# 三、数字:

# 0 分: 没有数字

# 10 分: 1 个数字

# 20 分: 大于1 个数字

# 四、符号:

# 0 分: 没有符号

# 10 分: 1 个符号

# 25 分: 大于1 个符号

# 五、奖励:

# 2 分: 字母和数字

# 3 分: 字母、数字和符号

# 5 分: 大小写字母、数字和符号

# 最后的评分标准:

# >= 90: 非常安全

# >= 80: 安全（Secure）

# >= 70: 非常强

# >= 60: 强（Strong）

# >= 50: 一般（Average）

# >= 25: 弱（Weak）

# >= 0:  非常弱


# 对应输出为：

# VERY_SECURE

# SECURE,

# VERY_STRONG,

# STRONG,

# AVERAGE,

# WEAK,

# VERY_WEAK,


# 请根据输入的密码字符串，进行安全评定。

# 注：

# 字母：a-z, A-Z

# 数字：-9

# 符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)

# !"#$% and '()*+,-./     (ASCII码：x21~0x2F)

# :;<=>?@             (ASCII<=><=><=><=><=>码：x3A~0x40)

# [\]^_`              (ASCII码：x5B~0x60)

# {|}~                (ASCII码：x7B~0x7E)




# 输入描述：
# 本题含有多组输入样例。
# 每组样例输入一个string的密码

# 输出描述：
# 每组样例输出密码等级

def getPWDScore(pwd):
    score = 0
    if len(pwd) >= 8:
        score +=25
    elif len(pwd) >=5:
        score += 10
    elif len(pwd) >=1:
        score += 5
 
    alphaLower= 0
    alphaUpper= 0
    digit = 0
    others = 0

    for i in pwd:
        if i.isalpha():
            if i.islower():
                alphaLower +=1
            else:
                alphaUpper +=1
        elif i.isdigit():
            digit += 1
        else:
            others += 1

    if alphaUpper !=0 and alphaLower != 0:
        score +=20
    elif alphaLower ==0 and alphaLower ==0:
        score +=0
    else:
        score+=10
   
    if digit>1:
        score+=20
    elif digit==1:
        score+=10
   
    if others>1:
        score+=25
    elif others ==1:
        score+=10

    if alphaUpper and alphaLower and digit and others:
        score+=5
    elif alphaLower and digit and others or alphaUpper and digit and others:
        score+=3
    elif alphaUpper and digit or alphaLower and digit:
        score+=2 
    return score

while True:
    try:
        pwd = input()
        num = getPWDScore(pwd)
        tiers = {
            'tier1':90,
            'tier2':80,
            'tier3':70,
            'tier4':60,
            'tier5':50,
            'tier6':25,
            'tier7':0,
        }
        strength = {
            'tier1':'VERY_SECURE',
            'tier2':'SECURE',
            'tier3':'VERY_STRONG',
            'tier4':'STRONG',
            'tier5':'AVERAGE',
            'tier6':'WEAK',
            'tier7':'VERY_WEAK',
        }
        if(num>=tiers.get('tier1')):
            print(strength.get('tier1'))
        elif num>= tiers.get('tier2'):
            print(strength.get('tier2'))
        elif num>= tiers.get('tier3'):
            print(strength.get('tier3'))
        elif num>= tiers.get('tier4'):
            print(strength.get('tier4'))
        elif num>= tiers.get('tier5'):
            print(strength.get('tier5'))
        elif num>= tiers.get('tier6'):
            print(strength.get('tier6'))
        elif num>= tiers.get('tier7'):
            print(strength.get('tier7'))            
    except:
        break