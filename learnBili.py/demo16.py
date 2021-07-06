import os
print(os.getcwd())
lst=os.listdir('chap6')
print(lst)
# os.mkdir('newdir')
os.makedirs('A/B/C')
os.rmdir('A/B/C')
os.removedirs('A/B/C')
os.chdir('chap6')

