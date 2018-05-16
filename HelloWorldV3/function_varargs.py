#coding=utf-8

def total(a=5,*numbers,**phonebook):
    print('a',a)

    r=0

    for single_item in numbers:
        print('single_item',single_item)
        r += 1

    for first_part,second_part in phonebook.items():
        print(first_part,second_part)
        r += 1

    return r

def some_function():
    pass

result=total(10,1,2,3,4,Jack=12312,john="adfad",Inged="324234")
print(result)

print(some_function())