num=int(input())

lst =[] 
for i in range(num):
    lst.append(str(input()))
# lst.sort()
# for i in lst:
#     print(i)
for i in sorted(lst):
    print(i)