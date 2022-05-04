'''
1. first input : size of 'numbers' list
2. Then enter all element for the list
3. Enter number of 'queries'
4. Enter number of query, which is 3. Each query element [x, y, z] means, from x's index to y's index sum from the 'numbers' list. Then add 'z' if specified range
includes '0's

ex) 
3       ----> size of 'numbers' list, 3
5       ----> next three represent elements of 'numbers' list.
10            This case, it is [5, 10, 10]
10
1       ----> number of query, 1
3
1 2 5   ----> It create query [[1, 2, 5]]

Output of this example should be 15. Query [1, 2, 5], so it sum up all numbers from 1st to 2nd index of [5, 10, 10], which is 5 + 10 =15. But within this range,
there is no '0' in between so we do not add [5] in the end.

ex2)
2       ----> size of 'numbers' list, 2
-5      ----> next three represent elements of 'numbers' list.
0             This case, it is [-5, 0]
2       ----> number of query, 2
3
2 2 20  ----> It create query [[2, 2, 20], [1, 2, 10]]
1 2 10

Output of this example should be 
20
5

'''



def findSum(numbers, queries):

    lst = []
    lst_final = []
    for i in range(len(queries)):
        for j in range(queries[i][0], queries[i][1]+1):
            try:
                lst.append(numbers[j-1])
            except:
                pass
        if 0 in lst:
            res = sum(lst) + queries[i][2]
        else:
            res = sum(lst)
        lst_final.append(res)
        lst = []

    return(lst_final)

if __name__ == '__main__':
    fptr = sys.stdout

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
