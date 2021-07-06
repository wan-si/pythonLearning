def reverseWithDSeparator(string):
    for i in string:
        # if (i < 'A') or ((i >'Z') and (i < 'a')) or (i >'z'):
        if not i.isalpha():
            string = string.replace(i," ")
    strList = string.split(' ')
    return strList[::-1]
try:
    while True:
        string = input()
        result = reverseWithDSeparator(string)
        print(' '.join(result))
except:
    pass        