# def conbainKey(nums,lst):
#     for i in range(nums):


nums=int(input())
dic = {}
for i in range(nums):
    data = input().split(' ')
    key = int(data[0])
    value = int(data[1])
    dic[key] = dic.get(key,0) + value
for i in sorted(dic):
    print(i,dic.get(i))    



