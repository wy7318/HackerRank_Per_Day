'''
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be

ex)
IN:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
OUT:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    ss = ""
    for i in word_list:
        ss += i + "\n"
    return(ss)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
