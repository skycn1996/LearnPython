#coding=utf-8

x=50

def func():
    global x
    print('x is ',x)
    x=2
    print('change global x to ',x)

func()
print('value of x is ',x)


def func2(y):
	global x
	print('x is ',x)
	x=y
	print('x is ?',x)


func2(12)
print('value of x is still 2? ',x,sep=':')
