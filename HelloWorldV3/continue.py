#coding=utf-8

while True:
    s=input("Enter something:")
    if s=="quit":
        break
    if len(s)<3:
        print('Too small')
        continue
    print('Input is out sufficient length:{0}'.format(len(s)))
