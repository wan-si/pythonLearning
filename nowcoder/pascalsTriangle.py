def pascalTriangle(nline):
    if nline <= 2:
        return -1
    elif nline%2 == 1:    
            return 2
    elif nline%4 == 0:
        return 3
    else:
        return 4
try:
    n=int(input())        
    print(pascalTriangle(n))
except:
    pass