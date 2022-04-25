'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
ex)
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
'''
def swap_case(s):
    lst = []
    for i in s:
        if i.islower():            
            lst.append(i.upper())
        else:            
            lst.append(i.lower())
    return "".join(lst)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
