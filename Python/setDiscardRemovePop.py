'''
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

INPUT:
The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.
ex)
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
OUTPUT : 4
'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input()
    lst_com = command.split()
    if lst_com[0] == 'remove':
        try:
            s.remove(int(lst_com[1]))
        except:
            pass
    elif lst_com[0] == 'discard':
        s.discard(int(lst_com[1]))
    else:
        try:
            s.pop()
        except:
            pass
print(sum(s))
