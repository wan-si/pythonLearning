def checkpassword(pwd):
    count=0
    if len(pwd)<=8:
        return False
    c_str = [pwd[i:i+3] for i in range(len(pwd)) if i+3 <= len(pwd)]
    if len(c_str)>len(set(c_str)):
        return False
    for s in pwd:
        if s.isdigit():
            count +=1
            break
    for  s in pwd:
        if not s.isdigit() and (s.lower()<'a' or s.lower()>'z'):
            count +=1
            break            
    for  s in pwd:
        if s.isupper():
            count +=1
            break
    for s in pwd:
        if s.islower():
            count += 1
            break
    if count >= 3:
        return True
    else:
        return False
try:
    while True:
        pw = input()
        if checkpassword(pw):
            print('OK')
        else:
            print('NG')
except:
    pass