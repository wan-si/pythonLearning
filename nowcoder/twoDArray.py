while True:
    try:
        m,n = map(int,input().split())
        x1,y1,x2,y2 = map(int,input().split())
        x = int(input())
        y = int(input())
        xx,yy = map(int,input().split())
        
        if(m>9 or n>9 or m<0 or n<0):
            print(-1)
        else:
            print(0)
        
        if(x1>m-1 or x1<0 or y1>n-1 or y1<0 or x2 >m-1 or x2<0 or y2>n-1 or y2<0):
            print(-1)
        else:            
            print(0)
        
        if(x>m-1 or m+1>9 or x< 0):
            print(-1)
        else:
            print(0)
        if(y>n-1 or n+1>9 or y<0):
            print('******')
            print(-1)
        else:
            print('-----')
            print(0)
        if(xx>m-1 or xx< 0 or yy>n-1 or yy<0):
            print(-1)
        else:
            print(0)
    except:
        break       
