def count_substring(string, sub_string):
    count = 0
    while True:
        x = string.find(sub_string)
        if x>=0:
            count+=1
            string = string[x+1:]
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)