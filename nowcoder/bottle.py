def getSodaTotal(nums):
    if(nums <= 1):
        return 0
    getSoda = 0
    while nums>=3:
        getSoda += (int(nums/3)) 
        nums = int(nums/3)+(nums%3)
    if(nums==2):
        getSoda +=1
    return getSoda
try:
    while True:
        nums=int(input())
        soda =getSodaTotal(nums)
        print(soda)    
except:
    pass        
