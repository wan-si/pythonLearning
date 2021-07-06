import sys 
lines=[]
for i in range(2):
    lines.append(sys.stdin.readline().strip()) 
string = lines[0]   
substring=lines[1]
# print(len(string))
# print(print(substring))
# list = string[::len(substring)]
list=[]
count=0
if len(string)<=0 or len(substring)<=0 or len(string) < len(substring) or string == None or substring == None:
    print('No')  
else:
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            print(i+1)
            count +=1
    if count == 0:
        print('No')       
    


        
# print(list)
# for i in list:
#     print(i)
# print(substring)