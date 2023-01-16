if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    grade = sorted(list(set([i[1] for i in records])))

    lowest_grade = sorted([i[0] for i in records if(i[1] == grade[1])])

    for i in lowest_grade:
        print(i)