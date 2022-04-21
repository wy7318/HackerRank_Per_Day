'''
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, 
lowercase and uppercase characters.

Output:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
'''
def identifier(inp, lst, func, length):
    for i in inp:
        if func(i):
            lst.append(True)
            break
    if len(lst) == length:
        lst.append(False)

if __name__ == '__main__':
    s = input()
    lst = []
    identifier(s, lst, str.isalnum, 0)
    identifier(s, lst, str.isalpha, 1)
    identifier(s, lst, str.isdigit, 2)
    identifier(s, lst, str.islower, 3)
    identifier(s, lst, str.isupper, 4)
    
   

    for i in lst:
        print(i)
