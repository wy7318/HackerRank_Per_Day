'''Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range 2 of 5 to , print Not Weird
If n is even and in the inclusive range 6 of 20 to , print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer n.
1<= n <= 100
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 == 1:
        print("Weird")
    elif n%2 == 0 and 2<= n <= 5:
        print("Not Weird")
    elif n%2 == 0 and 6<= n <= 20:
        print("Weird")
    elif n%2 == 0 and 20 < n <= 100:
        print("Not Weird")
   
