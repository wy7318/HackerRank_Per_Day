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
if __name__ == '__main__':
    s = input()
    lst = []
    for i in range(len(s)):
        if s[i].isalnum() == True:
            lst.append(True)
            break
    if len(lst) == 0:
        lst.append(False)
    
    for i in range(len(s)):
        if s[i].isalpha() == True:
            lst.append(True)
            break
    if len(lst) == 1:
        lst.append(False)
    
    for i in range(len(s)):
        if s[i].isdigit() == True:
            lst.append(True)
            break
    if len(lst) == 2:
        lst.append(False)
    
    for i in range(len(s)):
        if s[i].islower() == True:
            lst.append(True)
            break
    if len(lst) == 3:
        lst.append(False)
        
    for i in range(len(s)):
        if s[i].isupper() == True:
            lst.append(True)
            break
    if len(lst) == 4:
        lst.append(False)

    for i in lst:
        print(i)
