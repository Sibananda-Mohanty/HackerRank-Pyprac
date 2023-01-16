if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for a in range(N):
        command, *args = input().split()
            
        if command == "print":
            print(my_list)
        elif command == "insert":
            idx, obj = args
            my_list.insert(int(idx), int(obj))
        elif command == "remove":
            my_list.remove(int(args[0]))
        elif command == "append":
            my_list.append(int(args[0]))
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            a = my_list.pop()
        elif command == "reverse":
            my_list.reverse()