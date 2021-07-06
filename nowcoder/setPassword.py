def setPassword(pwd):
    actualPwd = str()
    for s in pwd:
        if s.isupper():
            actualPwd += chr(ord(s.lower())+1) if chr(ord(s.lower())+1)<='z' else  chr(ord(s.lower())+1 - 26)     
        elif s.islower():
            if(s >= 'a'and s<='c'):    
                actualPwd += '2'
                
            elif(s >= 'd'and s<='f'):
                actualPwd += '3'
                
            elif(s >= 'g'and s<='i'):
                actualPwd += '4'
                
            elif(s >= 'j'and s<='l'):
                actualPwd += '5' 
            elif(s >= 'm'and s<='n'):
                actualPwd += '6'                 
                
            elif(s >= 'p'and s<='s'):
                actualPwd += '7'
                    
            elif(s >= 't'and s<='u'):
                actualPwd += '8'  
            elif(s >= 'w'and s<='z'):
                actualPwd += '9'                                  
        else:
            actualPwd += s
    return actualPwd
try:
    while True:
        pwd = input()  
        actualPwd = setPassword(pwd)
        print(actualPwd)
except:
    pass        