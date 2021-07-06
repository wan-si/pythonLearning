# 根据输入的日期，计算是这一年的第几天。
def isLeap(year):
    if (year%4==0 and year%100 != 0) or (year%400 ==0):
        return True 
    

def getDay(year,month,day):
    dayOfMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    dayOfMonthLeap =[31,29,31,30,31,30,31,31,30,31,30,31]
    # totalDay = 0
    monthDay = 0
    if isLeap(year):
        for i in range(12):
            if(month > i+1):
                monthDay += dayOfMonthLeap[i]
    else:
        for i in range(12):
            if(month > i+1):
                monthDay += dayOfMonth[i]
    return monthDay+day

while True:
    try:
        year,month,day = map(int,input().split())
        print(getDay(year,month,day))
    except:
        break



