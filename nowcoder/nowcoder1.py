
def getInteger(floatNums):
    return round(floatNums)

    

def getInteger2(floatNums):
    
    dec = floatNums%1
    num =int(floatNums-dec)
    return num if(dec<0.5) else (num+1)


# floatNums = float(input())
# print(getInteger2(floatNums))
print (int(round(float(input()))))