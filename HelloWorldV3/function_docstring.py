#coding=utf-8

def print_max(x,y):
    '''打印两个数值中的最大数

    :param x: 整数
    :param y: 整数
    :return: None
    '''

    x=int(x)
    y=int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')

print_max(3,5)
print(print_max.__doc__)
help(print_max)