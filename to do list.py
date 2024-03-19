print('*'*80)
print("\t\t\t\t TO DO LIST")
print('*'*80)
b=[]
print(' Hello user welcome!!  \n 1) CREATE TASK \n 2) UPDATE TASK \n 3) TRACK TASK \n 4) exit')
while(True):
    a=int(input('enter your preference:  '))
    if a==1:
        n=int(input('please enter the number of tasks that you want to add to do list:  '))
        for i in range(n):
            c=input('enter the task:  ')
            b.append(c)
        print('sucessfully added tasks to to do list')
    elif a==2:
        print('\t\t\t\t """"" TO DO LIST """""')
        for j in range (len(b)):
            print("\t\t\t \t",b[j])
        y=int(input('\n"press 1 if you want to add task to TO DO LIST "\n"press 2 if you want to remove task from TO DO LIST"\n'))
        if y==1:
            x=input('enter the task that needs to be added to TO DO LIST  :')
            b.append(x)
        elif y==2:
            d=input(' enter the task  that needs to be deleted from the list \n please type without any changes like that in list :')
            b.remove(d)
        print('updated TO DO LIST')
        
    elif a==3:
        print(' \t\t\t tasks pending  in TO DO LIST')
        for j in range (len(b)):
            print("\t\t\t",b[j])
    else:
        break

