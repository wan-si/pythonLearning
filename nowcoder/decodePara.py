while True:
    try:
        stringList = input().split()
        # qcount = 0 
        list = []
        string = ''
        for i in stringList:
            qcount = i.count('"')
            if qcount%2 ==0:
                string += i.strip('"')
                list.append(string)
                string,qcount = '',0
            else:
                string += i.strip('"') + ' '
        print(len(list))
        for i in list:
            print(i)

                


            

        # string = input()
        # if string.__contains__('\"'):    
        #     stringList = string.split('\"')
        #     print(len(stringList))
        # # print('\n')
        #     for i in stringList: 
        #         print(i.strip())
        # else:
        #     stringList = string.split()
        #     print(len(stringList))
        #     for i in stringList:
        #         print(i)
                
    except:
         break