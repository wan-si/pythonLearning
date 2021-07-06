# 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。

# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。

# 例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。s

# 输入n，请输出n以内(含n)完全数的个数。计算范围, 0 < n <= 500000

# 本题输入含有多组样例。

# def getAliquotDivisor(nums):
#     count = 0
#     for i in range(1,nums+1):
#         if i ==1:
#             count += 1
#         sum = 0
#         for j in range(1,i):
#             if(nums%j==0):
#                 sum += j
#         if sum == nums:
#             count +=1        
#     return count

def isPerfectNumber(nums):
    sum = 0
    for i in range(1,nums):        
        if(nums%i==0):
            sum += i
    if sum == nums:
        return True

while True:
    try:
        count = 0
        n = int(input())
        for i in range(1,n+1):
            if isPerfectNumber(i):
                count += 1
        print(count)        
    except:
        break    


