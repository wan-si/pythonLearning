def main():
    while True:
        menum()
        choice=in(input('请选择'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice ==0:
                answer==input('您确定要推出系统吗？y/n')
                if answer=='y' or answer=='Y':
                    print('感谢您的使用！')
                    exit()
                    else:
                        continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()                
            elif choice==5:
                sort()
            elif choice==6:
                total()  
            elif choice==7:
                show()                            

def menum():
    print('=======学生信息管理系统=========')
    print('-----------功能菜单--------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生信息')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
def insert():
    pass
def search():
    
    