'''
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example
n=5
Print the string 12345.
'''

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(str(i+1))
        
    print(''.join(lst))
