if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        main_list.append([name, score])
set_1 = sorted({score for [name,score] in main_list})
name_list = [name for [name,score] in sorted(main_list, key = lambda x : x[0]) if score == set_1[1]]
x = [print(i) for i in name_list]