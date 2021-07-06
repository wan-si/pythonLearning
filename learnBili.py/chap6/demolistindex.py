lst=['hello','world',98,'hello']
print(lst.index('hello')) #如果列表中有相同元素，只返回列表中相同元素的第一个
print(lst.index('hello',1,3))#从开始到结束索引获取元素

print(lst[2])#正向从0～n-1
print(lst[-3])#逆向从-1～-n
print(lst[10])
