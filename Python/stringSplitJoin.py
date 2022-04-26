'''
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
ex) 
INPUT
this is a string   
OUTPUT
this-is-a-string
'''

def split_and_join(line):
    lst = line.split(" ")
    return "-".join(lst)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
