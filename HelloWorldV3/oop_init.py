class Person:
	def __init__(self,name):
		self.name=name
	def say_hi(self):
		print('hello,my name is ', self.name)

p=Person('Swaroop')
p.say_hi()

import sys
for i in sys.argv:
	Person(i).say_hi()
