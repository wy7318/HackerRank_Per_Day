'''
Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:

if i is multiple of both 3 and 5, print FizzBuzz
if i is a multiple of 3 (but not 5), print Fizz
if i is a multiple of 5(but not 3), print Buzz.
if i is not a multiple of 3 or 5, print i
'''

def fizzBuzz(n):
    for i in range(1,n+1):
        fizz = 'Fizz' if i%3 == 0 else ''
        buzz = 'Buzz' if i%5 == 0 else ''
        print(fizz + buzz or i)
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
