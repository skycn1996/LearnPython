#coding=utf-8

for i in range(1,5):
    print(i)
    if i==4:
        break
else:
    print('The for loop is over')

for i in range(1,5,2):
    print(i)
else:
    print('The for loop is over')

for i in list(range(5)):
    print(i)
else:
    print('List for loop is over')
