# file = open('b.txt','w')
file = open('c.txt','a')
lst=['java','go','python']
file.writelines(lst)
file.close()