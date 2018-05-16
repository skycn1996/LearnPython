if __name__=='__main__':
	print('The program is being run by itself')
else:
	print('I am being import from another module')

import sys

print('The command line arguments are:')

for i in sys.argv:
	print(i)
print('\n\nThe PYTHONPATH is',sys.path,'\n')

import os
print(os.getcwd())

from math import sqrt
print('Square root of 16 is',sqrt(16))
