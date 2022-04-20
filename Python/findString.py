'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

ex)
IN : 
ABCDCDC
CDC

OUT : 2
'''
def count_substring(string, sub_string):
    lst = []
    cnt = 0
    for i in range(len(string)):
        lst.append(string[i:len(sub_string) + i])
    for i in range(len(lst)):
        if lst[i] == sub_string:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
