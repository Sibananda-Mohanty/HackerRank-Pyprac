def mutate_string(string, position, character):
    string = list(string)
    position = int(position)
    string[position] = character
    text = ""
    for x in string:
        text += x      
    return text

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)