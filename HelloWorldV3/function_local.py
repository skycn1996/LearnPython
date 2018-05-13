#coding=utf-8

x=59

def func(x):
    print('x is ',x)
    x=2
    print('changed local x to ',x)

func(x)
print('x is still',x)