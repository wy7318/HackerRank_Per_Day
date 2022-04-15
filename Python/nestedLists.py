'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    lst_name = []
    lst_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst_name.append(name)
        lst_score.append(score)


    sortedScore = sorted(lst_score, reverse=True)
    minScore = min(sortedScore)
    for a in sortedScore:
        if a <= minScore:
            minScore = a
            continue
        else:
            secondMin = a
    lst_idx = []
    for b in range(len(lst_score)):
        if lst_score[b] == secondMin:
            lst_idx.append(b)
    sortedNames = []
    for c in range(len(lst_idx)):
        sortedNames.append(lst_name[lst_idx[c]])
    sortedNames.sort()
    for d in sortedNames:
        print(d)
