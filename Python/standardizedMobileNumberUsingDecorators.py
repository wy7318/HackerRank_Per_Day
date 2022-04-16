'''
Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

Sample Input:
3
07895462130
919875641230
9195969878

Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
'''

def wrapper(f):
    def fun(l):
        lst = []
        for i in range(len(l)):
            if len(l[i]) == 10:
                newP = l[i]
                lst.append(newP)
            elif len(l[i]) == 11:
                newP = l[i][1:]
                lst.append(newP)
            elif len(l[i]) == 12:
                newP = l[i][2:]
                lst.append(newP)
            elif len(l[i]) == 13:
                newP = l[i][3:]
                lst.append(newP)
        lst.sort()
        for i in lst:
            print("+91 " + i[:5] + " " + i[5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
