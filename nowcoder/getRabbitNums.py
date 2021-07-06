def getRabbitNums(month):
    if(month<=2):
        return 1
    return getRabbitNums(month-1)+getRabbitNums(month-2)

try:
   while True: 
    month = int(input())
    nums = getRabbitNums(month)
    print(nums)
except:
    pass    
        

    
