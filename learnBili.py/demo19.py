import os
path=os.getcwd()
lst_file = os.walk(path)
print(lst_file)
for dirpath,dirname,filename in lst_file:
    print(dirpath)
    print(dirname)
    print(filename)
    print('---------')