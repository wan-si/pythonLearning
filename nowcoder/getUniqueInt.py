num =list(input())
res = ''
for i in range(len(num)-1,-1,-1):
    if num[i] not in res:
        res += num[i]
# res = list(set(num))
print(res)
        
        


    