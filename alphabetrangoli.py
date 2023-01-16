def print_rangoli(size):
    # your code goes here
    letters = 'abcdefghijklmnopqrstuvwxyz'
    base = letters[:size]
    row_length = 4 * size - 3
    result = []
    for i in range(1, size + 1):
        row = '-'.join(base[-i:][1:][::-1] + base[-i:])
        row = row.center(row_length, '-') + '\n'
        result += [row]
        
    print(''.join(result + result[:-1][::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)