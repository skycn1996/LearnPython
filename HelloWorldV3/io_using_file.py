poem = '''\
programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')
lineno = 0 
while True:
    line = f.readline()
    if len(line) == 0:
        break
    lineno += 1
    print(lineno,line,end='')
f.close();
