def removeChr(string):
    dic = {}
    for s in string:
        if s not in dic:
            dic[s]=string.count(s)
    for s in sorted(dic.values):
        string.


        